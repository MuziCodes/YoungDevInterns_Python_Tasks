import streamlit as st

name = "Muzammil Ahmed"
title = "Software Engineer | Data Scientist"
email = "muzidxb1@gmail.com"
linkedin = "linkedin.com/in/mewzi"
github = "github.com/muzicodes"
summary = """\

As a tech-enthusiast speaking English, Urdu and Arabic., I have years of experience with practical projects and leadership roles throughout my university life. AI and data science are my keen interests given the adaptability, integrity, honesty, and perseverance I posses. My favourite methods to pass time are researching, reading books, programming and playing basketball. Ultimately, my biggest life interest is applying my technical expertise to help other individuals and organisations.As a tech-enthusiast speaking English, Urdu and Arabic., I have years of experience with practical projects and leadership roles throughout my university life. AI and data science are my keen interests given the adaptability, integrity, honesty, and perseverance I posses. My favourite methods to pass time are researching, reading books, programming and playing basketball. Ultimately, my biggest life interest is applying my technical expertise to help other individuals and organisations.
"""

skills = [
    "Programming: Python, Java, C, C++, MySQL, JavaScript/HTML/CSS",
    "Data Science: Visualization (Pandas, NumPy, Matplotlib, Seaborn) and web scraping (BeautifulSoup, Selenium)",
    "Version Control: GitHub",
    "ICT: Microsoft Office, Google Suite, Windows, Linux",
]

experience = [
    {
        "title": "Manager",
        "company": "DerekSol",
        "duration": "Nov 2024 - Present (1 month)",
        "location": "Remote",
        "details": "Administrative Organization and Marketing"
    },
    {
        "title": "Python Developer",
        "company": "YoungDev Intern",
        "duration": "Oct 2024 - Present (2 months)",
        "location": "Remote",
        "details": "Web Hosting and Development",
    },
]

education = [
    {
        "degree": "Bachelor's in Software Engineering",
        "institution": "Usman Institute of Technology",
        "duration": "Feb 2024 – Dec 2027",
        "details": "Skills: Figma (Software), IT Operations, and +3 skills",
    },
    {
        "degree": "Software Engineering (Hons)",
        "institution": "University of Stirling",
        "duration": "Sep 2023 – Nov 2023",
        "details": "Activities and Societies: Scored 90/100 in the first quiz of Scripting for Data Science\nSkills: PHP, Eclipse, Python, Java and MySQL",
    },

    {
        "degree": "Bachelor's in Computer Science",
        "institution": "National University of Computer and Emerging Sciences",
        "duration": "Aug 2022 – Jun 2023",
        "details": """Activities: Top 10 in speed eating competition, A* at Seerah competition from MIRC""",
        "Skills": """OOP, Microsoft PowerPoint, MySQL, Microsoft Excel, C++, Adobe Acrobat, IT Operations, Communication, Microsoft Word, C""",
    },
    {
        "degree": "A Level",
        "institution": "The Westminster School, Dubai",
        "duration": "2020 – 2022",
        "details": """Activities: Won first place at inter-school hadith competition, several coding competitions, started translating books, worked with 4 YouTube channels""",
        "Leadership": """Head of Islamic Education for 12A""",
        "Skills": """Adobe Acrobat, Communication, Python""",
    },
    {
        "degree": "IGCSE",
        "institution": "The Westminster School, Dubai",
        "duration": "May 2017 – Jun 2020",
        "details": "Grade: 4 A*s and 3 As",
        "Activities": "Bronze medal at basketball, 13 certificates of merit, 1st runner-up at Amity University competition",
        "Leadership": """Head of Multimedia Club (Grade 9), Vice President of Grade 9B5, Assessment Coordinator (Grade 10), Head of Physics (Grade 11)""",
    },
    {
        "degree": "KG2 - Grade 1",
        "institution": "Little Flower English School, Dubai",
        "duration": "2007 – 2009",
        "details": """Activities: 2nd place in annual running competition, played football, participated in field trips""",
        "Skills": "Communication",
    },
]


st.set_page_config(page_title="Digital Resume", page_icon=":briefcase:", layout="wide")

st.title(name)
st.subheader(title)
st.write(f"[Email](mailto:{email}) | [LinkedIn](https://{linkedin}) | [GitHub](https://{github})")

st.header("Summary")
st.write(summary)

st.header("Skills")
st.write(" - " + "\n - ".join(skills))

st.header("Experience")
for exp in experience:
    st.subheader(exp["title"] + " - " + exp["company"])
    st.write(f"**{exp['duration']}**")
    st.write(exp["details"])

st.header("Education")
for edu in education:
    st.subheader(edu["degree"] + " - " + edu["institution"])
    st.write(f"**{edu['duration']}**")
    st.write(edu["details"])
