import streamlit as st

def main():
    st.title("Can you become a rising star or senior student? Check your eligibility")
    
    with st.form(key='student_form'):
        # Basic details
        name = st.text_input("Name")
        roll = st.text_input("Roll No")
        email = st.text_input("Email")
        
        # Assignment completion options
        q1_assignment = st.radio("Quarter 1 assignment completed", ["Yes", "No"])
        q2_assignment = st.radio("Quarter 2 assignment completed", ["Yes", "No"])
        hackathon = st.radio("Hackathon marketplace completed", ["Yes", "No"])
        
        # Time slot selection
        slot = st.selectbox("Select time slot", 
                            ["Monday 2 to 5", "Tuesday 7 to 10", "Wednesday 7 to 10", 
                             "Thursday 9 to 12", "Friday 9 to 12", "Saturday 9 to 12", 
                             "Saturday 2 to 5", "Saturday 7 to 10"])
        
        submit = st.form_submit_button("Submit")
    
    if submit:
        # Display user details
        if not (name and roll and email):
            st.error("Please fill all the required fields: Name, Roll, and Email.")
        else:
            st.subheader("Student Details:")
            st.write("*Name:*", name)
            st.write("*Roll No:*", roll)
            st.write("*Email:*", email)
            st.write("*Quarter 1 assignment completed:*", q1_assignment)
            st.write("*Quarter 2 assignment completed:*", q2_assignment)
            st.write("*Hackathon marketplace completed:*", hackathon)
            st.write("*Selected Time Slot:*", slot)
            
            # Eligibility check based on assignment options
            if q1_assignment == "Yes" and q2_assignment == "Yes" and hackathon == "Yes":
                st.success("Congratulations you are eligible to be a rising star/ senior student")
            else:
                st.error("No, you are not eligible to be a Rising Star or Senior Student.")

main()