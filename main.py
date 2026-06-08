import streamlit as st
import os 
from services.auth.login_wall import render_login_wall
from services.state.session_defualts import initial_session_defaults
from services.config.workout_config import EXERCISE_OPTIONS
from services.ui.style_loader import inject_local_fonts,load_css
def main():
    st.set_page_config(page_title="AI Real-time Gym Coach", page_icon="🏋️‍♀️",
                       initial_sidebar_state="collapsed",
                       layout="centered",
                    )
    load_css(os.path.join(os.getcwd(),"static","style.css"))
    inject_local_fonts(os.path.join(os.getcwd(),"static","Gelasio-Bold.ttf"),"Gelasio-Bold")



    if not render_login_wall():
        return
    initial_session_defaults()

    workout_started=st.session_state.get("workout_started",False)

    with st.sidebar:
        st.title("Gym Tutor")
        st.caption(f"Training of {st.session_state.username}")

        if not workout_started:
            st.selectbox("Select Exercise",options=EXERCISE_OPTIONS,key="plan_exercise")
            st.number_input("Sets",min_value=0,max_value=50,step=1,key="plan_sets")
            st.number_input("Reps per set",min_value=0,max_value=50,key="plan_reps",step=1)

            st.markdown("")
            start_session_button=st.button("Start Workout",width="stretch",key="start_session_button")
            if start_session_button:
                st.session_state["workout_started"]=True
                st.rerun()
        else:
            exercise=st.session_state.get("plan_exercise")
            sets=st.session_state.get("plan_sets")
            reps=st.session_state.get("plan_reps")
        
            st.info(f"**{exercise}** -- {sets}/{reps}")

            end_session_button=st.button("End Workout",width="stretch",key="end_session_button")

            if end_session_button:
                st.session_state["workout_started"]=False
                st.rerun()

        if workout_started:
            st.divider()

            exercise=st.session_state.get("plan_exercise")
            total_reps=st.session_state.get("reps")
            current_set_reps=st.session_state.get("current_set_reps")
            reps_per_set=st.session_state.get("plan_reps")
            sets_completed=st.session_state.get("sets_completed")
            target_sets=st.session_state.get("plan_sets")


            st.subheader("Progress")

            st.metric("Total Reps", total_reps)
            st.metric("Current Set reps", f"{current_set_reps}/{reps_per_set}")
            st.metric("Sets Completed", f"{sets_completed}/{target_sets}")

            st.divider()

            if (exercise=="Squats"):
                st.subheader("Squat Metrics")
                st.metric("Knee Angle", f"{st.session_state.knee_angle}°")
                st.metric("Back Angle", f"{st.session_state.back_angle}°")
                st.metric("Depth Status", st.session_state.hip_status)


            elif (exercise=="Push-ups"):
                st.subheader("Push-up Metrics")
                st.metric("Elbow Angle", f"{st.session_state.elbow_angle}°")
                st.metric("Body Alignment", f"{st.session_state.body_alignment}°")
                st.metric("Hip Position", st.session_state.hip_status)

            elif (exercise=="Lunges"):
                st.subheader("Lunges Metrics")
                st.metric("Front Knee Angle", f"{st.session_state.front_knee_angle}°")
                st.metric("Torso Angle", f"{st.session_state.torso_angle}°")
                st.metric("Balance Status", st.session_state.balance_status)

            elif(exercise=="bicep curls"):
                st.subheader("Bicep Curls Metrics")
                st.metric("Elbow Angle", f"{st.session_state.elbow_angle}°")
                st.metric("Shoulder Stability", st.session_state.shoulder_status)
                st.metric("Swing Detection", st.session_state.swing_status)

            elif(exercise=="Shoulder Press"):
                st.subheader("Shoulder Press Metrics")
                st.metric("Elbow Angle", f"{st.session_state.elbow_angle}°")
                st.metric("Arm Extension", st.session_state.extension_status)
                st.metric("Back Arch Detection", st.session_state.back_arch_status)


                
                 




    
    

if __name__ == "__main__":
    main()

