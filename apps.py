import streamlit as st
import pandas as pd
import importlib.util
import os

script_dir = 'C:\\Users\\Administrator\\Desktop\\Miniproj\\venv\\Scripts'
spec_db = importlib.util.spec_from_file_location("database", os.path.join(script_dir, "database.py"))
database = importlib.util.module_from_spec(spec_db)
spec_db.loader.exec_module(database)
Database = database.Database

class StreamlitApp:
    def __init__(self):
        self.db = Database()

    def display_table(self, df):
        st.table(df.style.set_properties(**{'background-color': '#f2f2f2'}))

    def eligibility_criteria(self):
        st.title(":rainbow[Eligibility Criteria]")
        problems_solved = st.number_input("Problems Solved >=", min_value=0, value=50)
        mock_interview_score = st.number_input("Mock Interview Score >=", min_value=0, value=75)
        if st.button("Fetch Eligible Students"):
            try:
                query = """ 
                SELECT s.*, p.problems_solved, pl.mock_interview_score 
                FROM students s 
                JOIN programming p ON s.student_id = p.student_id 
                JOIN placements pl ON s.student_id = pl.student_id 
                WHERE p.problems_solved >= %s AND pl.mock_interview_score >= %s 
                """
                df_eligible_students = self.db.fetch_data(query, (problems_solved, mock_interview_score))
                if df_eligible_students is not None and not df_eligible_students.empty:
                    st.write("Eligible Students:")
                    self.display_table(df_eligible_students)
                else:
                    st.write(":red[No eligible students found]")
            except Exception as e:
                st.write(f":red[An error occurred: {e}]")

    def insights(self):
        st.title(":orange[Insights]")
        try:
            insights = self.db.fetch_insights()
            if insights is not None:
                insights_list = [
                    {"title": "Total Students:", "key": "total_students"},
                    {"title": "All Student Info:", "key": "all_student_info"},
                    {"title": "Problems Solved Greater Than 50:", "key": "problems_solved_greater_than_50"},
                    {"title": "Highest Mock Interview Score:", "key": "highest_mock_interview_score"},
                    {"title": "Lowest Problems Solved:", "key": "lowest_problems_solved"},
                    {"title": "Average Problems Solved:", "key": "avg_problems_solved"},
                    {"title": "Mock Interview Score Greater Than 75:", "key": "mock_interview_score_greater_than_75"},
                    {"title": "Total Problems Solved:", "key": "total_problems_solved"},
                    {"title": "Students Per Batch:", "key": "students_per_batch"},
                    {"title": "Student Info With Problems Solved And Mock Score:", "key": "student_info_with_problems_solved_and_mock_score"}
                ]

                for insight in insights_list:
                    st.write(insight["title"])
                    if insight["key"] in insights and insights[insight["key"]] is not None:
                        if isinstance(insights[insight["key"]], pd.DataFrame):
                            if insights[insight["key"]].shape[1] == 1 and insights[insight["key"]].shape[0] == 1:
                                st.write(insights[insight["key"]].iloc[0, 0])
                            else:
                                self.display_table(insights[insight["key"]])
                        else:
                            st.write(insights[insight["key"]])
                    else:
                        st.write(f"No data found for {insight['title']}.")
            else:
                st.write("No insights found")
        except Exception as e:
            st.write(f":red[An error occurred: {e}]")

def main():
    st.set_page_config(layout="wide", page_title="Placement Eligibility Apps", page_icon=":smiley:")
    app = StreamlitApp()
    if not app.db.connect():
        st.write(":red[Failed to connect to database]")
        return
    try:
        pages = {
            "Eligibility Criteria": app.eligibility_criteria,
            "Insights": app.insights
        }
        page = st.sidebar.selectbox("Choose a page", list(pages.keys()))
        pages[page]()
    except Exception as e:
        st.write(f":red[An error occurred: {e}]")
    finally:
        app.db.disconnect()

if __name__ == "__main__":
    main()
