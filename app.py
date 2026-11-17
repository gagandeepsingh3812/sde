import streamlit as st
import pandas as pd

st.title("Student Record Management System")

# Store student records
if "students" not in st.session_state:
    st.session_state.students = pd.DataFrame(
        columns=["Roll No", "Name", "Age", "Course"]
    )

# Menu
menu = st.sidebar.selectbox(
    "Select Operation",
    ["Add Student", "View Students", "Update Student", "Delete Student"]
)

# CREATE
if menu == "Add Student":

    st.header("Add Student")

    roll = st.number_input("Roll Number", min_value=1, step=1)
    name = st.text_input("Student Name")
    age = st.number_input("Age", min_value=1, max_value=100)
    course = st.text_input("Course")

    if st.button("Add Student"):

        if name and course:

            if roll in st.session_state.students["Roll No"].values:
                st.error("Roll Number already exists!")

            else:
                new_student = pd.DataFrame([{
                    "Roll No": roll,
                    "Name": name,
                    "Age": age,
                    "Course": course
                }])

                st.session_state.students = pd.concat(
                    [st.session_state.students, new_student],
                    ignore_index=True
                )

                st.success("Student Added Successfully!")

        else:
            st.warning("Please enter all details.")

# READ
elif menu == "View Students":

    st.header("All Student Records")

    st.dataframe(st.session_state.students)

# UPDATE
elif menu == "Update Student":

    st.header("Update Student")

    if not st.session_state.students.empty:

        roll = st.selectbox(
            "Select Roll Number",
            st.session_state.students["Roll No"]
        )

        student = st.session_state.students[
            st.session_state.students["Roll No"] == roll
        ].iloc[0]

        name = st.text_input("Name", value=student["Name"])
        age = st.number_input("Age", value=int(student["Age"]))
        course = st.text_input("Course", value=student["Course"])

        if st.button("Update"):

            index = st.session_state.students[
                st.session_state.students["Roll No"] == roll
            ].index[0]

            st.session_state.students.loc[index, "Name"] = name
            st.session_state.students.loc[index, "Age"] = age
            st.session_state.students.loc[index, "Course"] = course

            st.success("Student Updated Successfully!")

    else:
        st.warning("No student records available.")

# DELETE
elif menu == "Delete Student":

    st.header("Delete Student")

    if not st.session_state.students.empty:

        roll = st.selectbox(
            "Select Roll Number",
            st.session_state.students["Roll No"]
        )

        if st.button("Delete"):

            st.session_state.students = (
                st.session_state.students[
                    st.session_state.students["Roll No"] != roll
                ].reset_index(drop=True)
            )

            st.success("Student Deleted Successfully!")

    else:
        st.warning("No student records available.")