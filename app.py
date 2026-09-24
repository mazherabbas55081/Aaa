import streamlit as st
from datetime import date

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Bright Future School",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# PREMIUM CSS
# =========================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

* {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background: #f5f7fb;
    color: #172033;
}

.block-container {
    max-width: 1400px;
    padding-top: 1rem;
}

/* HERO */
.hero {
    min-height: 500px;
    border-radius: 30px;
    padding: 70px 7%;
    display: flex;
    align-items: center;
    color: white;

    background:
        linear-gradient(
            105deg,
            rgba(4,18,40,.97),
            rgba(9,54,105,.75)
        ),
        url("https://images.unsplash.com/photo-1562774053-701939374585?auto=format&fit=crop&w=1800&q=90");

    background-size: cover;
    background-position: center;

    box-shadow: 0 25px 70px rgba(8,26,51,.25);

    position: relative;
    overflow: hidden;
}

.hero:after {
    content: "";
    position: absolute;
    width: 430px;
    height: 430px;
    border-radius: 50%;
    right: -150px;
    top: -160px;
    background: rgba(23,195,255,.18);
}

.hero-content {
    position: relative;
    z-index: 2;
    max-width: 760px;
}

.badge {
    display: inline-block;
    padding: 9px 16px;
    border-radius: 50px;
    background: rgba(255,255,255,.1);
    border: 1px solid rgba(255,255,255,.25);
    font-size: 12px;
    letter-spacing: 1px;
}

.hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(44px, 6vw, 78px);
    line-height: 1.03;
    margin: 20px 0;
}

.hero p {
    font-size: 18px;
    line-height: 1.7;
    color: #dbe8fb;
}

.stats {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    margin-top: 28px;
}

.stat {
    background: rgba(255,255,255,.1);
    padding: 14px 20px;
    border-radius: 16px;
    border: 1px solid rgba(255,255,255,.15);
}

.stat b {
    display: block;
    font-size: 25px;
}

.stat span {
    font-size: 12px;
    color: #c7d7ee;
}

/* SECTIONS */
.section {
    padding: 48px 0 12px;
}

.kicker {
    color: #1767ff;
    font-weight: 700;
    letter-spacing: 2px;
    font-size: 12px;
    text-transform: uppercase;
}

.title {
    font-family: 'Playfair Display', serif;
    color: #081a33;
    font-size: 40px;
    margin: 5px 0 10px;
}

.subtitle,
.muted {
    color: #718096;
    line-height: 1.7;
}

/* CARDS */
.card {
    background: #fff;
    border: 1px solid #e6ebf2;
    border-radius: 22px;
    padding: 25px;
    box-shadow: 0 12px 32px rgba(20,45,80,.06);
    height: 100%;
}

.icon {
    width: 54px;
    height: 54px;
    border-radius: 16px;
    background: #eaf2ff;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 25px;
}

/* TEACHERS */
.teacher {
    background: #fff;
    border: 1px solid #e6ebf2;
    border-radius: 22px;
    padding: 12px;
    box-shadow: 0 10px 28px rgba(0,0,0,.05);
}

.teacher img {
    width: 100%;
    height: 250px;
    object-fit: cover;
    border-radius: 17px;
}

.teacher-info {
    padding: 10px;
}

.teacher-info h4 {
    margin: 0;
    color: #081a33;
}

.teacher-info p {
    margin: 5px 0;
    color: #718096;
}

/* GALLERY */
.gallery {
    background: white;
    border: 1px solid #e6ebf2;
    border-radius: 22px;
    padding: 12px;
    box-shadow: 0 10px 28px rgba(0,0,0,.05);
}

.gallery img {
    width: 100%;
    height: 250px;
    object-fit: cover;
    border-radius: 17px;
}

/* NOTICES */
.notice {
    background: white;
    border-left: 5px solid #1767ff;
    border-radius: 14px;
    padding: 17px 20px;
    margin: 10px 0;
    box-shadow: 0 6px 20px rgba(0,0,0,.04);
}

/* EVENTS */
.event {
    display: flex;
    gap: 15px;
    align-items: center;

    background: white;
    border: 1px solid #e5ebf3;
    border-radius: 18px;

    padding: 14px;
    margin: 10px 0;
}

.event-date {
    min-width: 64px;
    text-align: center;
    background: #081a33;
    color: white;
    border-radius: 13px;
    padding: 9px;
}

.event-date b {
    font-size: 23px;
    display: block;
}

.event-date span {
    font-size: 11px;
    color: #b8d2ff;
}

/* FORM */
div[data-testid="stForm"] {
    background: white;
    border: 1px solid #e3e8f1;
    border-radius: 22px;
    padding: 24px;
}

/* BUTTON */
.stButton > button {
    border-radius: 12px;
    font-weight: 700;
    min-height: 44px;
}

/* METRICS */
div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e5eaf2;
    padding: 16px;
    border-radius: 17px;
}

/* FOOTER */
.footer {
    margin-top: 60px;
    padding: 45px;
    background: #081a33;
    color: #b9c9df;
    border-radius: 28px 28px 0 0;
}

.footer h3 {
    color: white;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# DATA
# =========================================================

teachers = [
    (
        "Dr. Sarah Ahmed",
        "Principal",
        "https://images.unsplash.com/photo-1580894732444-8ecded7900cd?auto=format&fit=crop&w=700&q=85"
    ),
    (
        "Mr. Hamza Khan",
        "Mathematics",
        "https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=700&q=85"
    ),
    (
        "Ms. Ayesha Malik",
        "English",
        "https://images.unsplash.com/photo-1544717305-2782549b5136?auto=format&fit=crop&w=700&q=85"
    ),
    (
        "Mr. Usman Ali",
        "Computer Science",
        "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=700&q=85"
    )
]


gallery = [
    (
        "Campus",
        "https://images.unsplash.com/photo-1562774053-701939374585?auto=format&fit=crop&w=1200&q=90"
    ),
    (
        "Smart Classroom",
        "https://images.unsplash.com/photo-1580582932707-520aed937b7b?auto=format&fit=crop&w=1200&q=90"
    ),
    (
        "Students",
        "https://images.unsplash.com/photo-1509062522246-3755977927d7?auto=format&fit=crop&w=1200&q=90"
    ),
    (
        "Science Lab",
        "https://images.unsplash.com/photo-1532094349884-543bc11b234d?auto=format&fit=crop&w=1200&q=90"
    ),
    (
        "Library",
        "https://images.unsplash.com/photo-1507842217343-583bb7270b66?auto=format&fit=crop&w=1200&q=90"
    ),
    (
        "Sports",
        "https://images.unsplash.com/photo-1461896836934-ffe607ba8211?auto=format&fit=crop&w=1200&q=90"
    )
]


notices = [
    (
        "Admissions Open 2026–27",
        "Applications are open for Nursery to Grade 10.",
        "NEW"
    ),
    (
        "Parent–Teacher Meeting",
        "Monthly PTM will be held Saturday at 10:00 AM.",
        "IMPORTANT"
    ),
    (
        "Annual Sports Gala",
        "Inter-house sports registration is open.",
        "EVENT"
    ),
    (
        "Scholarship Program",
        "Merit-based scholarships are available.",
        "SCHOLARSHIP"
    )
]


events = [
    ("12", "OCT", "Annual Sports Gala", "Main Ground"),
    ("21", "OCT", "Science Exhibition", "Science Block"),
    ("05", "NOV", "Parents Day", "Auditorium"),
    ("18", "NOV", "Educational Trip", "Murree")
]


# =========================================================
# HEADER
# =========================================================

a, b, c, d, e = st.columns([2.7, 1, 1, 1, 1])

with a:
    st.markdown("### 🎓 Bright Future School")

with b:
    st.button("Home", use_container_width=True)

with c:
    st.button("About", use_container_width=True)

with d:
    st.button("Academics", use_container_width=True)

with e:
    st.button("Contact", use_container_width=True)


# =========================================================
# HERO
# =========================================================

st.markdown("""
<div class="hero">

<div class="hero-content">

<span class="badge">
✨ PREMIUM EDUCATION • EST. 1998
</span>

<h1>
Where Future Leaders Begin.
</h1>

<p>
Empowering students with knowledge, character, creativity
and technology in a safe, inspiring and world-class
learning environment.
</p>

<div class="stats">

<div class="stat">
<b>25+</b>
<span>Years Excellence</span>
</div>

<div class="stat">
<b>2,500+</b>
<span>Students</span>
</div>

<div class="stat">
<b>120+</b>
<span>Expert Teachers</span>
</div>

<div class="stat">
<b>98%</b>
<span>Success Rate</span>
</div>

</div>

</div>
</div>
""", unsafe_allow_html=True)


# =========================================================
# WHY US
# =========================================================

st.markdown("""
<div class="section">
<span class="kicker">Why Choose Us</span>
<div class="title">Education beyond the classroom.</div>
<p class="subtitle">
A balanced ecosystem designed to help every learner discover their potential.
</p>
</div>
""", unsafe_allow_html=True)


features = [
    ("🎯", "Personalized Learning",
     "Student-centered teaching and individual support."),

    ("🧪", "Modern Labs",
     "Hands-on science, technology and innovation facilities."),

    ("🏆", "Character Building",
     "Leadership, confidence, teamwork and responsibility."),

    ("💻", "Digital Campus",
     "Smart classrooms and technology-enabled learning.")
]


cols = st.columns(4)

for col, (icon, title, description) in zip(cols, features):

    with col:

        st.markdown(
            f"""
            <div class="card">

            <div class="icon">
            {icon}
            </div>

            <h3>{title}</h3>

            <p class="muted">
            {description}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# CAMPUS
# =========================================================

st.markdown("""
<div class="section">
<span class="kicker">Our Campus</span>
<div class="title">A place designed for curiosity.</div>
</div>
""", unsafe_allow_html=True)


x, y = st.columns([1.1, 1])

with x:

    st.image(
        gallery[2][1],
        use_container_width=True
    )


with y:

    st.markdown("""
    <div class="card">

    <h3>
    Learning that prepares students for tomorrow
    </h3>

    <p class="muted">
    Bright Future School combines strong academics with
    arts, sports, technology and community service.
    </p>

    <p class="muted">
    Our campus encourages questions, collaboration,
    creativity, communication and independent thinking.
    </p>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# ACADEMICS
# =========================================================

st.markdown("""
<div class="section">
<span class="kicker">Academics</span>
<div class="title">Programs for every stage.</div>
</div>
""", unsafe_allow_html=True)


programs = [

    ("🌱", "Early Years",
     "Nursery • KG",
     "Play-based foundations."),

    ("📘", "Primary School",
     "Grades 1–5",
     "Core academics and creativity."),

    ("🔬", "Middle School",
     "Grades 6–8",
     "STEM, languages and research."),

    ("🎓", "Secondary School",
     "Grades 9–10",
     "Board preparation and advanced subjects.")
]


cols = st.columns(4)

for col, (icon, title, grades, description) in zip(cols, programs):

    with col:

        st.markdown(
            f"""
            <div class="card">

            <div class="icon">
            {icon}
            </div>

            <h3>{title}</h3>

            <b>{grades}</b>

            <p class="muted">
            {description}
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# TEACHERS
# =========================================================

st.markdown("""
<div class="section">
<span class="kicker">Our Faculty</span>
<div class="title">Meet our educators.</div>
</div>
""", unsafe_allow_html=True)


cols = st.columns(4)

for col, (name, role, image) in zip(cols, teachers):

    with col:

        st.markdown(
            f"""
            <div class="teacher">

            <img src="{image}">

            <div class="teacher-info">

            <h4>{name}</h4>

            <p>{role}</p>

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# NOTICES + EVENTS
# =========================================================

st.markdown("""
<div class="section">
<span class="kicker">School Life</span>
<div class="title">Latest updates.</div>
</div>
""", unsafe_allow_html=True)


left, right = st.columns([1.15, 1])


with left:

    st.subheader("📢 Notices")

    for title, description, tag in notices:

        st.markdown(
            f"""
            <div class="notice">

            <b>{title}</b>

            <small>
            • {tag}
            </small>

            <br>

            <span class="muted">
            {description}
            </span>

            </div>
            """,
            unsafe_allow_html=True
        )


with right:

    st.subheader("📅 Upcoming Events")

    for day, month, title, place in events:

        st.markdown(
            f"""
            <div class="event">

            <div class="event-date">

            <b>{day}</b>

            <span>{month}</span>

            </div>

            <div>

            <b>{title}</b>

            <br>

            <span class="muted">
            📍 {place}
            </span>

            </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# GALLERY
# =========================================================

st.markdown("""
<div class="section">
<span class="kicker">Gallery</span>
<div class="title">Moments that matter.</div>
</div>
""", unsafe_allow_html=True)


for row in [gallery[:3], gallery[3:]]:

    cols = st.columns(3)

    for col, (caption, image) in zip(cols, row):

        with col:

            st.markdown(
                f"""
                <div class="gallery">

                <img src="{image}">

                </div>

                <p style="text-align:center;font-weight:700">
                {caption}
                </p>
                """,
                unsafe_allow_html=True
            )


# =========================================================
# ADMISSION FORM
# =========================================================

st.markdown("""
<div class="section">

<span class="kicker">Admissions</span>

<div class="title">
Start your journey.
</div>

</div>
""", unsafe_allow_html=True)


with st.form("admission_form"):

    col1, col2 = st.columns(2)

    with col1:

        student = st.text_input(
            "Student Full Name *"
        )

        parent = st.text_input(
            "Parent / Guardian *"
        )

        dob = st.date_input(
            "Date of Birth",
            date(2015, 1, 1)
        )

    with col2:

        email = st.text_input(
            "Email *"
        )

        phone = st.text_input(
            "Phone *"
        )

        grade = st.selectbox(
            "Applying For",
            [
                "Nursery",
                "KG",
                "Grade 1",
                "Grade 2",
                "Grade 3",
                "Grade 4",
                "Grade 5",
                "Grade 6",
                "Grade 7",
                "Grade 8",
                "Grade 9",
                "Grade 10"
            ]
        )

    address = st.text_area(
        "Home Address"
    )

    submit = st.form_submit_button(
        "🚀 Submit Admission Application",
        use_container_width=True
    )

    if submit:

        if student and parent and email and phone:

            st.success(
                f"Application received for {student}."
            )

        else:

            st.warning(
                "Please complete all required fields."
            )


# =========================================================
# STUDENT DASHBOARD
# =========================================================

st.markdown("""
<div class="section">

<span class="kicker">
Student Portal
</span>

<div class="title">
Dashboard preview.
</div>

</div>
""", unsafe_allow_html=True)


m1, m2, m3, m4 = st.columns(4)


m1.metric(
    "Attendance",
    "94%",
    "+2.1%"
)

m2.metric(
    "Average Grade",
    "A",
    "Excellent"
)

m3.metric(
    "Assignments",
    "18 / 20",
    "90%"
)

m4.metric(
    "Fee Status",
    "Paid",
    "Current"
)


p, q = st.columns(2)


with p:

    st.markdown("""
    <div class="card">

    <h3>
    📊 Academic Results
    </h3>

    <p class="muted">

    Mathematics — A+<br>
    English — A<br>
    Science — A+<br>
    Computer Science — A<br>
    Social Studies — A

    </p>

    </div>
    """, unsafe_allow_html=True)


with q:

    st.markdown("""
    <div class="card">

    <h3>
    💳 Fee Information
    </h3>

    <p class="muted">

    Tuition: PKR 18,000<br>
    Transport: PKR 4,000<br>
    Activity Fund: PKR 1,500<br><br>

    <b>
    Total: PKR 23,500
    </b>

    </p>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# CONTACT
# =========================================================

st.markdown("""
<div class="section">

<span class="kicker">
Contact
</span>

<div class="title">
We would love to hear from you.
</div>

</div>
""", unsafe_allow_html=True)


p, q = st.columns(2)


with p:

    with st.form("contact_form"):

        name = st.text_input(
            "Your Name"
        )

        email2 = st.text_input(
            "Email"
        )

        message = st.text_area(
            "Message"
        )

        send = st.form_submit_button(
            "Send Message",
            use_container_width=True
        )

        if send:

            st.success(
                "Message submitted successfully."
            )


with q:

    st.markdown("""
    <div class="card">

    <h3>📍 Visit Campus</h3>

    <p class="muted">
    123 Education Avenue, Main City
    </p>

    <h3>📞 Call Us</h3>

    <p class="muted">
    +92 300 1234567
    </p>

    <h3>✉️ Email</h3>

    <p class="muted">
    info@brightfutureschool.edu
    </p>

    <h3>🕘 Office Hours</h3>

    <p class="muted">
    Monday–Friday: 8:00 AM – 3:00 PM
    </p>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

<h3>
🎓 Bright Future School
</h3>

<p>
Learn • Lead • Inspire
</p>

<p>
© 2026 Bright Future School.
All rights reserved.
</p>

</div>
""", unsafe_allow_html=True)
