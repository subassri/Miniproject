import pymysql
import pandas as pd
import logging
import os

class Database:
    def __init__(self):
        self.host = None
        self.user = None
        self.password = None
        self.database = None
        self.conn = None
        self.load_config()

    def load_config(self):
        # Load database configuration
        script_dir = os.path.dirname(__file__)
        env_path = os.path.join(script_dir, "placed.env")
        config = {}
        with open(env_path, "r") as f:
            for line in f:
                key, value = line.strip().split("=")
                config[key] = value
        self.host = config["DB_HOST"]
        self.user = config["DB_USER"]
        self.password = config["DB_PASSWORD"]
        self.database = config["DB_NAME"]

    def connect(self):
        try:
            self.conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            return True
        except Exception as e:
            logging.error(f"Failed to connect to database: {e}")
            return False

    def disconnect(self):
        if self.conn:
            self.conn.close()

    def fetch_data(self, query, params=None):
        try:
            df = pd.read_sql_query(query, self.conn, params=params)
            return df
        except Exception as e:
            logging.error(f"Failed to fetch data: {e}")
            return None

    def fetch_insights(self):
        insights = {}
        try:
            QUERY_TOTAL_STUDENTS = """ SELECT COUNT(*) FROM students; """
            insights['total_students'] = self.fetch_data(QUERY_TOTAL_STUDENTS)

            QUERY_ALL_STUDENT_INFO = """ SELECT * FROM students; """
            insights['all_student_info'] = self.fetch_data(QUERY_ALL_STUDENT_INFO)

            QUERY_PROBLEMS_SOLVED_GREATER_THAN_50 = """ SELECT * FROM programming WHERE problems_solved > 50; """
            insights['problems_solved_greater_than_50'] = self.fetch_data(QUERY_PROBLEMS_SOLVED_GREATER_THAN_50)

            QUERY_HIGHEST_MOCK_INTERVIEW_SCORE = """ SELECT MAX(mock_interview_score) FROM placements; """
            insights['highest_mock_interview_score'] = self.fetch_data(QUERY_HIGHEST_MOCK_INTERVIEW_SCORE)

            QUERY_LOWEST_PROBLEMS_SOLVED = """ SELECT MIN(problems_solved) FROM programming; """
            insights['lowest_problems_solved'] = self.fetch_data(QUERY_LOWEST_PROBLEMS_SOLVED)

            QUERY_AVG_PROBLEMS_SOLVED = """ SELECT AVG(problems_solved) FROM programming; """
            insights['avg_problems_solved'] = self.fetch_data(QUERY_AVG_PROBLEMS_SOLVED)

            QUERY_MOCK_INTERVIEW_SCORE_GREATER_THAN_75 = """ SELECT * FROM placements WHERE mock_interview_score > 75; """
            insights['mock_interview_score_greater_than_75'] = self.fetch_data(QUERY_MOCK_INTERVIEW_SCORE_GREATER_THAN_75)

            QUERY_TOTAL_PROBLEMS_SOLVED = """ SELECT SUM(problems_solved) FROM programming; """
            insights['total_problems_solved'] = self.fetch_data(QUERY_TOTAL_PROBLEMS_SOLVED)

            QUERY_STUDENTS_PER_BATCH = """ SELECT course_batch, COUNT(*) FROM students GROUP BY course_batch; """
            insights['students_per_batch'] = self.fetch_data(QUERY_STUDENTS_PER_BATCH)

            QUERY_STUDENT_INFO_WITH_PROBLEMS_SOLVED_AND_MOCK_SCORE = """ SELECT s.*, p.problems_solved, pl.mock_interview_score FROM students s JOIN programming p ON s.student_id = p.student_id JOIN placements pl ON s.student_id = pl.student_id; """
            insights['student_info_with_problems_solved_and_mock_score'] = self.fetch_data(QUERY_STUDENT_INFO_WITH_PROBLEMS_SOLVED_AND_MOCK_SCORE)

            return insights
        except Exception as e:
            logging.error(f"Failed to fetch insights: {e}")
            return None
