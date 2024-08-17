import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import base64
import requests

# Function to load Lottie animations from a URL
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Main function to define the layout and content of the Streamlit app
def main():
    st.set_page_config(
        layout="wide",
        page_icon="🎓",
        page_title="Berat Tuğberk Günel - Portfolio"
    )

    # Load Lottie animations
    lottie_about_me = load_lottie_url("https://lottie.host/1586fa64-a195-4ab6-a3c6-99f4d77ac85b/boAazJbefK.json")
    lottie_projects = load_lottie_url("https://lottie.host/216f304a-3ec9-45ba-a435-3ed81f2e6c4c/EfwarHOuxN.json")
    lottie_contact = load_lottie_url("https://lottie.host/c32ec37e-8c1c-4969-9deb-63cb7ea89350/03ncnNsz6g.json")
    
    # Custom CSS for Lottie Integration
    st.markdown("""
        <style>
            .lottie-container {
                width: 100%;
                height: 300px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Custom CSS
    st.markdown("""
        <style>
            h1 {
                color: orange;
                font-family: 'Arial', sans-serif;
                font-size: 38px;
            }
            h2 {
                color: orange;
                font-family: 'Arial', sans-serif;
                font-size: 32px;
            }
            h3 {
                color: #C49549;
                font-family: 'Arial', sans-serif;
                font-size: 26px;
            }
            h4 {
                color: #C49549;
                font-family: 'Arial', sans-serif;
                font-size: 24px;
            }
            p {
                color: #FFFFFF;
                font-family: 'Arial', sans-serif;
                font-size: 20px;
            }
            a {
                color: #2980B9;
                text-decoration: none;
                font-weight: bold;
            }
            a:hover {
                color: #FF5733;
                text-decoration: underline;
            }
            .divider {
                margin: 20px 0;
                height: 1px;
                background-color: #DDDDDD;
            }
            .container {
                padding: 20px;
                background-color: #1C2126;
                border-radius: 10px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }
            .form-container {
                padding: 20px;
                background-color: #1C2126;
                border-radius: 10px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }
            .form-container input, .form-container textarea {
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #DDDDDD;
                border-radius: 5px;
                font-family: 'Arial', sans-serif;
            }
            .form-container button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-family: 'Arial', sans-serif;
                font-size: 16px;
            }
            .form-container button:hover {
                background-color: #45A049;
            }
        </style>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap='small', vertical_alignment='center')

    with col1:
        # Header Section
        st.markdown("""
            <h1>Greetings 👋</h1>
            <h2>Welcome to My Personal Portfolio</h2>
            """, 
        unsafe_allow_html=True)

        cv_file = "CV.pdf"  
        trans_file = "Transcript.pdf"

        try:

            with open(cv_file, "rb") as cv:
                cv_data = cv.read()
            
            b64_cv = base64.b64encode(cv_data).decode()
            to_cv = f'<a href="data:application/octet-stream;base64,{b64_cv}" download="Resume_BTGUNEL.pdf">Resume</a>'
        
        except:
            to_cv = '<strong style="color: red;">The resume is not available is not available</strong>'


        try:
            with open(trans_file, "rb") as tra:
                trans_data = tra.read()

            b64_trans = base64.b64encode(trans_data).decode()
            to_trans = f'<a href="data:application/octet-stream;base64,{b64_trans}" download="Transcript_BTGUNEL.pdf">Transcript</a>'
        
        except:
            to_trans = '<strong style="color: red;">The transcript is not available is not available</strong>'


        st.markdown(f"""
            <div style='text-align: justify;'>
                <p>Hi, it is Berat Tuğberk Günel. I'm currently pursuing a Master's degree at IFP School, specializing in Reservoir Geoscience and Engineering. 
                From a young age, I've been captivated by science, always eager to explore new ideas beyond my professional focus. 
                Lately, I've been diving into machine learning algorithms, aiming to integrate these cutting-edge solutions into the energy industry.</p>
            </div>
            <div style='text-align: justify;'>
                <p><a href="https://www.linkedin.com/in/berat-tuğberk-günel-928460173/">LinkedIn</a> | 
                <a href="https://github.com/guneltugberk">GitHub</a> | 
                <a href="https://scholar.google.com/citations?hl=tr&user=EHUbYYUAAAAJ&view_op=list_works&gmla=AC6lMd9do7qJIa3zNX2ZGa3fhhqz2yADJyGWJndn80RISWQy976ciMbAf-bgpKoHI41iRPYi5fSxA75U94LjTWp4IcKmfg">Google Scholar</a> | 
                {to_cv} |
                {to_trans} </p>
            </div>
            <div class="divider"></div>
        """, unsafe_allow_html=True)
    
    with col2:
        st_lottie(lottie_about_me, height=350)

    # Navigation Menu
    with st.container():
        selected = option_menu(
            menu_title=None,
            options=['About Me', 'Projects', 'Contact'],
            icons=['person', 'code-slash', 'chat-left-text-fill'],
            orientation='horizontal',
            styles={
                "container": {"padding": "0!important", "background-color": "#4C5258"},
                "icon": {"color": "orange", "font-size": "25px"}, 
                "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#838990"},
                "nav-link-selected": {"background-color": "#1C2126"},
            }
        )

    # About Section
    if selected == 'About Me':
        st.markdown("""
            <div class="container" style="text-align: center;">
                <h2>About Me</h2>
            </div>
            <br>
        """, unsafe_allow_html=True)

        cola, colb = st.columns(2, gap='small', vertical_alignment='center')

        with cola:
            st.markdown(f"""
                    <div class="container" style="width: 100%; height: 400px; max-width: 1500; min-width: 300px; margin: 0 auto;">
                        <div style="display: flex; gap: 30px;">
                            <div style="flex: 1;">
                                <h3 style="font-size: 22px; font-family: Arial, sans-serif; text-align: center;"><strong>Education</strong></h3>
                                <ul style="font-size: 18px; font-family: Arial, sans-serif;">
                                    <li><strong>IFP School</strong>
                                        <ul style="font-size: 16px; font-family: Arial, sans-serif;">
                                            <li>Master in Science, Reservoir Geoscience and Engineering</li>
                                        </ul>
                                    </li>
                                    <li><strong>Istanbul Technical University</strong>
                                        <ul style="font-size: 16px; font-family: Arial, sans-serif;">
                                            <li>Bachelor in Science, Petroleum Engineering</li>
                                            <li>GPA: 3.59/4.00</li>
                                        </ul>
                                    </li>
                                    <li><strong>Warsaw University of Technology</strong>
                                        <ul style="font-size: 16px; font-family: Arial, sans-serif;">
                                            <li>Energy Sources, Conversion, and Storage (Short Course)</li>
                                        </ul>
                                    </li>
                                    <li><strong>Technische Hochschule Georg Agricola</strong>
                                        <ul style="font-size: 16px; font-family: Arial, sans-serif;">
                                            <li>Sustainability and Resource Efficiency (Summer School)</li>
                                        </ul>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
        
        with colb:
            st.markdown(f"""
                    <div class="container" style="width: 100%; height: 400px; max-width: 1500; min-width: 300px; margin: 0 auto;">
                            <div style="display: flex; gap: 20px;">
                                <div style="flex: 1;">
                                    <h3 style="font-size: 22px; font-family: Arial, sans-serif; text-align: center;"><strong>Experience</strong></h3>
                                    <ul style="font-size: 18px; font-family: Arial, sans-serif;">
                                        <li><strong>Turkish Petroleum Offshore Technology Centre</strong>
                                            <ul style="font-size: 16px; font-family: Arial, sans-serif;">
                                                <li>Long Term Reservoir Engineering Intern (8 months)</li>
                                            </ul>
                                        </li>
                                        <li><strong>Baker Hughes</strong>
                                            <ul style="font-size: 16px; font-family: Arial, sans-serif;">
                                                <li>Well Completion and Intervention Intern (1.5 months)</li>
                                            </ul>
                                        </li>
                                        <li><strong>TU Bergakademie Freiberg</strong>
                                            <ul style="font-size: 16px; font-family: Arial, sans-serif;">
                                                <li>Summer Research Intern (2 months)</li>
                                            </ul>
                                        </li>
                                        <li><strong>Institute of Graduate School ITU</strong>
                                            <ul style="font-size: 16px; font-family: Arial, sans-serif;">
                                                <li>Part Time IT Consultant (5 months)</li>
                                            </ul>
                                        </li>
                                        <li><strong>Turkish Petroleum</strong>
                                            <ul style="font-size: 16px; font-family: Arial, sans-serif;">
                                                <li>Production Engineering Intern (2.5 months)</li>
                                            </ul>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                    </div>
                """, 
                unsafe_allow_html=True)

    # Projects Section
    if selected == 'Projects':
        st.markdown("""
            <div class="container" style="text-align: center;">
                <h2>Projects</h2>
            </div>
            <br>
        """, unsafe_allow_html=True)

        col3, col4 = st.columns(2, gap='small', vertical_alignment='center')
        
        with st.container(border=True):
            with col3:
                st_lottie(lottie_projects, height=350, key="Projects")

            with col4:
                grad_file = "Graduation.pdf"

                try:
                    with open(grad_file, "rb") as gra:
                        grad_data = gra.read()

                    b64_grad = base64.b64encode(grad_data).decode()
                    to_grad = f'<a href="data:application/octet-stream;base64,{b64_grad}" download="Graduation Project.pdf">Paper</a>'
                
                except:
                    to_grad = '<strong style="color: red;">The graduation project is not available is not available</strong>'


                st.markdown(f"""
                    <div class="container" style="text-align: justify;">
                        <div style="display: flex; gap: 40px;">
                            <div style="flex: 1; text-align: center;">
                                <ul style="font-size: 18px; font-family: Arial, sans-serif;">
                                    <li><strong style="font-size: 20px;">Full Field Development Project, A Case Study</strong>
                                        <ul style="font-size: 16px; font-family: Arial, sans-serif;">
                                            <li>Graduation Project | {to_grad}</li>
                                        </ul>
                                    </li>
                                    <li><strong style="font-size: 20px;">A Machine Learning Approach to Solids Content Estimation of Drilling Fluids</strong>
                                        <ul style="font-size: 16px; font-family: Arial, sans-serif;">
                                            <li>Project Website: <a href="https://beesolids.streamlit.app" style="color: #1E90FF;">Bee Solids Website</a></li>
                                        </ul>
                                    </li>
                                    <li><strong style="font-size: 20px;">Predicting Bottomhole Temperature of Offshore Production Wells in the North Sea</strong>
                                        <ul style="font-size: 16px; font-family: Arial, sans-serif;">
                                            <li>SPE Student Paper Contest, 2nd Place</li>
                                        </ul>
                                    </li>
                                    <li><strong style="font-size: 20px;">Data Driven Web Based Simulation for Geothermal Heat Pump Drilling Around Saxony, Germany</strong>
                                        <ul style="font-size: 16px; font-family: Arial, sans-serif;">
                                            <li>Project Website: <a href="https://drillingautomation.streamlit.app" style="color: #1E90FF;">Simulation Website</a> | Paper: <a href="https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2024/Ganel.pdf" style="color: #1E90FF;">Stanford Geothermal Workshop</a></li>
                                        </ul>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                """, unsafe_allow_html=True)

    # Contact Section
    if selected == 'Contact':
        st.markdown("""
            <div class="container" style="text-align: center;">
                <h2>Get in Touch with Me!</h2>
            </div>
            <br>
        """, unsafe_allow_html=True)
        col5, col6 = st.columns(2, gap='small', vertical_alignment='center')

        with col5:
            st.markdown("""
                <div class="container form-container">
                    <form action="https://formsubmit.co/berat-tugberk.gunel.2025@ifp-school.com" method="POST">
                        <input type="text" name="name" placeholder="Your Name" required>
                        <input type="email" name="email" placeholder="Your Email" required>
                        <textarea name="message" placeholder="Your Message" required></textarea>
                        <div style="text-align: center;">
                            <button type="submit" style="padding: 10px 20px; background-color: #4CAF50; color: white; border: none; border-radius: 5px; cursor: pointer;">
                                Send
                            </button>
                        </div>
                    </form>
                </div>
            """, unsafe_allow_html=True)


        with col6:
            st_lottie(lottie_contact, height=350)


if __name__ == '__main__':
    main()
