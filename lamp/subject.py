import pandas as pd 
import numpy as np
import datetime
import math
import lamp
from functools import reduce
#import

class Subject():
	"""
	Create subject dataframe
	
	"""
	def __init__(self, id, age=None, race=None, sex=None):
		self.id = id
		self.age = age
		self.race = race
		self.sex = sex
		self.df = self.create_subject_df()
		self.origina_df = self.create_subject_df()
		self.impute_status = False
		self.bin_status = False
		self.normalize_status = False
	
	def get_id(self):
		return self.id
	
	def get_age(self):
		return self.age
	
	def get_race(self):
		return self.race
	
	def get_sex(self):
		return self.sex
	
	def set_age(self, age):
		self.age = age
		
	def set_race(self, race):
		self.race = race
		
	def set_sex(self, sex):
		self.sex = sex
		
	def get_survey_results(self, participant=None):
		"""
		Get survey events for participant
		"""
		def survey_event_parse(survey):
			"""
			Helper function that parses survey event 

			Parameters:
			survey (list): contains all questions in particicular survey 

			Returns:
				survey_result (dict): maps relevant question categories to a score
			"""
			survey_result = {}
			for event in survey:
				question = event['item']

				#Check if question in one of the categories
				if question in lamp.SurveyQuestionDict:
					category = lamp.SurveyQuestionDict[question]

					#If reverse coded social question, then flip the score
					if category == "Social_Reverse":
						category = 'Social'
						score = 3 - event['value']
					elif category == 'Medication':
						score = 3 - event['value']
					else:
						score = event['value']

					if category in survey_result: survey_result[category].append(score) 
					else: survey_result[category] = [score]

			#Take mean for each cat
			for cat in survey_result:
				survey_result[cat] = float(sum(survey_result[cat])/len(survey_result[cat]))
			return survey_result 

		participant_surveys = {} #initialize dict mapping survey_type to occurence of scores
		if participant is None:
			participant = self.id
		participant_results = lamp.result_event.result_event_all_by_participant(participant).data
		for res in participant_results:
			#Check if its a survey event
			if 'survey_name' in res['static_data'].keys():
				try:
					survey_result = survey_event_parse(res['temporal_events'])
				except Exception as e:
					print(e)
					continue

				survey_time = res['timestamp']
				#Add to master dictionary
				for category in survey_result:
					if category not in participant_surveys:
						participant_surveys[category] = [(survey_result[category], survey_time)]
					else:
						participant_surveys[category].append((survey_result[category], survey_time))

		return participant_surveys
	
	def create_subject_df(self, beiwe_filepath='/home/ec2-user/Data/Beiwe/Processed/current_pipeline_output/Processed_Data/Individual/', ndays=90):
	
		subject_surveys = self.get_survey_results()
		#print(subject_surveys)

		#Find the first, last date
		try:
			first_day = datetime.datetime.utcfromtimestamp(sorted([subject_surveys[key][0][1]/1000 for key in subject_surveys])[0]).date()
			last_day = datetime.datetime.utcfromtimestamp(sorted([subject_surveys[key][-1][1]/1000 for key in subject_surveys])[-1]).date()
			number_of_days = (last_day - first_day).days
		except Exception as e:
			print(e)
			#print(self.id, subject_surveys)
			#return pd_DataFrame({'Date':[], 'id

		#Create dateframe, 90 days is standard
		df = pd.DataFrame({'Date': [first_day + datetime.timedelta(days=x) for x in range(min(90, number_of_days))], 'id':self.id})

		#Parse surveys
		for cat in subject_surveys:
			df[cat] = np.nan
			for event in subject_surveys[cat]:
				event_day = datetime.datetime.utcfromtimestamp(event[1]/1000).date()
				df.loc[df['Date'] == event_day, cat] = event[0]

		#Convert to Date to string
		df['Date'] = df['Date'].astype(str)

		#Take into account medication
		if 'Medication' not in list(df):
			df['Medication'] = [np.nan]*df.index.size


		#Try beta vals
		beta_val_list = pd.read_csv('/home/ec2-user/Data/LAMP Part 1/daily_beta_vals.csv')
		subj_beta_vals = beta_val_list.loc[beta_val_list['id'] == self.id]
		if subj_beta_vals.empty:
			df['beta_a'] = np.nan
			df['beta_b'] = np.nan
		else:
			df = pd.merge(df, subj_beta_vals[['Date', 'beta_a', 'beta_b']], on='Date')

		def parse_beiwe_pipeline(subject_id, beiwe_filepath, ndays=90):
			#Find beiwe id
			participant_data = pd.read_csv('/home/ec2-user/Data/LAMP Part 1/master_id_map.csv')
			beiwe_id = participant_data.loc[participant_data['id'] == subject_id, 'beiwe_id'].values[0]
			
			if not isinstance(beiwe_id, str):
				print('No beiwe file', subject_id)
				return None, None



			#Get step data

			try:
				steps_file = pd.read_csv(beiwe_filepath+beiwe_id+'/steps.csv')
				steps_file['Date'] = steps_file['Date'].astype(str)

			except Exception as e:
				print(e)
				steps_file = None

			#Get sleep_data
			try:
				sleep_file = pd.read_csv(beiwe_filepath+beiwe_id+'/sleep_estimates.csv')
				sleep_file['Date'] = sleep_file['Date'].astype(str)
			except:
				#print('No sleep file!')
				sleep_file = None

			return steps_file, sleep_file

		steps_file, sleep_file = parse_beiwe_pipeline(self.id, beiwe_filepath=beiwe_filepath)

		dataframes = [df]
		#print(dataframes)
		if steps_file is not None:
			dataframes.append(steps_file)

		if sleep_file is not None:
			dataframes.append(sleep_file)

		if steps_file is not None and sleep_file is not None:
			df_final = reduce(lambda left,right: pd.merge(left, right, on='Date', how='left'), dataframes)
		else:
			df_final = df
			
		return df_final
	
	def impute(self, columns):
		"""
		Get value for each column for each window
		"""
		if self.impute_status:
			print('Dataframe already imputed.')
			return

		weighted_dict = [0.05, 0.20, 0.40, 1.5, 0.4, 0.20, 0.05]

		#Get indices of all middle bin values; add them to new df
		for col in columns:
			col_values = []

			for ind in range(len(self.df.index)):

				#Get indices
				middle_weight_index = 3
				starting_index = max(ind -3, 0)
				ending_index = min(ind + 4, 90)

				#Get slice values
				subj_slice = self.df.iloc[starting_index:ending_index]

				#Remove na
				subj_slice_no_nan = subj_slice[col].dropna()
				slice_indices = subj_slice_no_nan.index

				if len(slice_indices) == 0:
					col_values.append(np.nan)
					continue

				#Match slice index with weight index
				weighted_dict_vals = [weighted_dict[middle_weight_index - (ind - slice_i)] for slice_i in slice_indices]

				#Find total in bin
				slice_val = sum(subj_slice_no_nan * [val / sum(weighted_dict_vals) for val in weighted_dict_vals])
				col_values.append(slice_val)

			self.df[col] = col_values
		
		self.impute_status = True

	
	def bin(self, columns, window_size=3):
		"""
		Bin dataframe
		"""

		self.df['bin'] = np.floor(self.df.index / window_size )
		bins = self.df.groupby('bin')

		subj_bin_df = pd.DataFrame(columns=['Bin Start Date', 'Bin End Date']+columns)
		for b in bins:
			bin_values = []
			#Add bin start/end dates
			start_date, end_date = b[1].iloc[0]['Date'], b[1].iloc[-1]['Date']
			bin_values.extend((start_date, end_date))
			for col in columns:
				if col in b[1].columns:
					bin_col_value = b[1][col].mean()
					bin_values.append(bin_col_value)
				else:
					bin_values.append(np.nan)

			#Add date range
			subj_bin_df.loc[b[0]] = bin_values    

		subj_bin_df['id'] = self.id

		return subj_bin_df
	
	def normalize(self, columns, col_means={}, col_vars={}):
		"""
		Normalize columns values to 0 mean/ unit variance
		:param col_means (dict): the mean for each column value
		:param col_vars (dict): the variance for each column value
		
		If mean/var not provided, resort to in-sample normalization
		"""
		if col_means == {} and col_vars == {}:
			for col in columns:
				if col in self.df:
					col_means[col] = self.df[col].mean()
					col_vars[col] = self.df[col].std()
		
		for col in columns:
			if col in self.df.columns:
				self.df[col] = (self.df[col] - col_means[col]) / col_vars[col]