# ============================================================
# SITE IDENTITY
# ============================================================
# Edit this section for the information that identifies you
# across the whole website.

SITE = {
    "name": "STUDIO/NAME",
    "role": "Multidisciplinary Artist & Mechanical Engineer",
    "title": "Portfolio — 3D & 2D Artist / Mechanical Engineer",
    "tagline": "Creative technology, visual storytelling, and mechanical design.",
    "description": (
        "Multidisciplinary portfolio covering 3D design, sculpting and animation, "
        "2D illustration, storyboarding and animation, and mechanical design."
    ),
    "email": "hello@example.com",
    "phone": "+00 000 000 000",
    "location": "Available worldwide · Remote",
    "availability": "Available for freelance & collaborations",
    "footer_name": "Your Name",
}


# ============================================================
# HERO
# ============================================================
# heading_html can contain HTML because the template intentionally
# renders it as markup. Keep the tags limited to the existing styles.

HERO = {
    "eyebrow": "Multidisciplinary creative",
    "heading_html": 'I build worlds in <span class="stroke">3D</span> & <span class="accent">2D</span> —<br>engineered for precision.',
    "subheading": (
        "Multidisciplinary artist & mechanical engineer. From concept sculpts and "
        "animation to production-ready CAD, I bridge creative storytelling with technical rigor."
    ),
    "primary_cta": {"text": "View my work →", "url": "#work"},
    "secondary_cta": {"text": "Start a project", "url": "#contact"},
    "stats": [
        {"number": "6+", "label": "Creative disciplines"},
        {"number": "B.Eng", "label": "Mechanical Engineering"},
        {"number": "2D+3D", "label": "Art & animation"},
    ],
}


# ============================================================
# DISCIPLINES
# ============================================================

DISCIPLINES = [
    {
        "icon": "🧊",
        "title": "3D Art & Animation",
        "description": (
            "High-detail sculpting, hard-surface and organic modeling, rigging and "
            "character/product animation built for film, games and visualization."
        ),
        "tags": ["Sculpting", "Modeling", "Texturing", "Rigging", "3D Animation"],
    },
    {
        "icon": "✏️",
        "title": "2D Art & Animation",
        "description": (
            "Illustration, concept art and storyboarding through to frame-by-frame "
            "and rigged 2D animation that gives ideas motion and narrative."
        ),
        "tags": ["Illustration", "Storyboarding", "Concept Art", "2D Animation"],
    },
    {
        "icon": "⚙️",
        "title": "Mechanical Design",
        "description": (
            "A Mechanical Engineering degree backing real product design — parametric "
            "CAD, assemblies, drawings and design-for-manufacture."
        ),
        "tags": ["SolidWorks", "AutoCAD", "CAD", "DFM"],
    },
]


# ============================================================
# PORTFOLIO
# ============================================================
# Add/edit projects here. Every project has descriptive metadata so
# the same content can later power cards, project pages, SEO metadata,
# search, or an API without rewriting the portfolio.

PORTFOLIO_CATEGORIES = {
    "3d": "3D Design",
    "sculpt": "Sculpting",
    "3danim": "3D Animation",
    "illus": "Illustration",
    "board": "Storyboarding",
    "2danim": "2D Animation",
    "mech": "Mechanical",
}

WORKS = [
    {
        "title": "Creature Bust — Sculpt",
        "slug": "creature-bust-sculpt",
        "category": "sculpt",
        "description": "High-detail character sculpt demonstrating organic modeling and sculpting workflow.",
        "image": "",
        "gradient": ["#ff5c38", "#a56bff"],
        "featured": True,
        "tools": ["ZBrush", "Blender"],
        "skills": ["Sculpting", "Organic Modeling", "Character Art"],
        "links": {"github": "", "demo": "", "case_study": ""},
    },
    {
        "title": "Sci-Fi Prop — Hard Surface",
        "slug": "sci-fi-prop-hard-surface",
        "category": "3d",
        "description": "Hard-surface 3D prop focused on clean forms, detail, materials and presentation.",
        "image": "",
        "gradient": ["#38b6ff", "#a56bff"],
        "featured": True,
        "tools": ["Blender", "Substance"],
        "skills": ["Hard Surface", "Modeling", "Texturing"],
        "links": {"github": "", "demo": "", "case_study": ""},
    },
    {
        "title": "Character Walk Cycle",
        "slug": "character-walk-cycle",
        "category": "3danim",
        "description": "Character animation study focused on rigging, timing, movement and performance.",
        "image": "",
        "gradient": ["#a56bff", "#ff5c38"],
        "featured": True,
        "tools": ["Blender"],
        "skills": ["Rigging", "3D Animation", "Character Animation"],
        "links": {"github": "", "demo": "", "case_study": ""},
    },
    {
        "title": "Editorial Illustration",
        "slug": "editorial-illustration",
        "category": "illus",
        "description": "Editorial illustration created to communicate an idea through composition and visual storytelling.",
        "image": "",
        "gradient": ["#ff5c38", "#ffb038"],
        "featured": False,
        "tools": ["Photoshop", "Procreate"],
        "skills": ["Illustration", "Concept Art", "Visual Storytelling"],
        "links": {"github": "", "demo": "", "case_study": ""},
    },
    {
        "title": "Short Film — Storyboard",
        "slug": "short-film-storyboard",
        "category": "board",
        "description": "Storyboard sequence developed to plan camera direction, action, pacing and visual continuity.",
        "image": "",
        "gradient": ["#38b6ff", "#3ddc84"],
        "featured": False,
        "tools": ["Photoshop", "Storyboard Tools"],
        "skills": ["Storyboarding", "Visual Development", "Pre-production"],
        "links": {"github": "", "demo": "", "case_study": ""},
    },
    {
        "title": "2D Animated Explainer",
        "slug": "2d-animated-explainer",
        "category": "2danim",
        "description": "2D animation project translating a concept into a clear, engaging visual sequence.",
        "image": "",
        "gradient": ["#a56bff", "#38b6ff"],
        "featured": False,
        "tools": ["After Effects", "Photoshop"],
        "skills": ["2D Animation", "Motion Design", "Visual Communication"],
        "links": {"github": "", "demo": "", "case_study": ""},
    },
    {
        "title": "Gearbox Assembly — SolidWorks",
        "slug": "gearbox-assembly-solidworks",
        "category": "mech",
        "description": "Parametric gearbox assembly demonstrating mechanical design, assembly structure and CAD workflow.",
        "image": "",
        "gradient": ["#9aa4b2", "#38b6ff"],
        "featured": True,
        "tools": ["SolidWorks"],
        "skills": ["Mechanical Design", "CAD", "Assemblies", "DFM"],
        "links": {"github": "", "demo": "", "case_study": ""},
    },
    {
        "title": "Stylized Environment",
        "slug": "stylized-environment",
        "category": "3d",
        "description": "Stylized 3D environment exploring modeling, composition, materials and lighting.",
        "image": "",
        "gradient": ["#3ddc84", "#38b6ff"],
        "featured": False,
        "tools": ["Blender"],
        "skills": ["Environment Art", "Modeling", "Materials"],
        "links": {"github": "", "demo": "", "case_study": ""},
    },
    {
        "title": "Concept Character Sheet",
        "slug": "concept-character-sheet",
        "category": "illus",
        "description": "Character concept development showing visual exploration, silhouettes and design direction.",
        "image": "",
        "gradient": ["#ff5c38", "#a56bff"],
        "featured": False,
        "tools": ["Photoshop", "Procreate"],
        "skills": ["Concept Art", "Character Design", "Illustration"],
        "links": {"github": "", "demo": "", "case_study": ""},
    },
    {
        "title": "Product Render — 3D Design",
        "slug": "product-render-3d-design",
        "category": "3d",
        "description": "Product-focused 3D design and rendering exercise emphasizing form, materials and presentation.",
        "image": "",
        "gradient": ["#38b6ff", "#ff5c38"],
        "featured": False,
        "tools": ["Blender", "Substance"],
        "skills": ["Product Visualization", "3D Modeling", "Rendering"],
        "links": {"github": "", "demo": "", "case_study": ""},
    },
    {
        "title": "Bracket — AutoCAD Drawing",
        "slug": "bracket-autocad-drawing",
        "category": "mech",
        "description": "Mechanical bracket drawing demonstrating technical drafting and dimensioning.",
        "image": "",
        "gradient": ["#9aa4b2", "#a56bff"],
        "featured": False,
        "tools": ["AutoCAD"],
        "skills": ["Technical Drawing", "Mechanical Design", "CAD"],
        "links": {"github": "", "demo": "", "case_study": ""},
    },
    {
        "title": "Fight Scene — Animatic",
        "slug": "fight-scene-animatic",
        "category": "board",
        "description": "Action animatic exploring shot composition, timing, movement and sequence planning.",
        "image": "",
        "gradient": ["#ffb038", "#ff5c38"],
        "featured": False,
        "tools": ["Storyboard Tools", "After Effects"],
        "skills": ["Storyboarding", "Animatics", "Action Planning"],
        "links": {"github": "", "demo": "", "case_study": ""},
    },
]


# ============================================================
# ABOUT
# ============================================================

ABOUT = {
    "title": "Where art meets engineering",
    "paragraphs": [
        "I’m a multidisciplinary creative with a <strong>Mechanical Engineering degree</strong> and a deep passion for visual storytelling. That mix lets me think like an engineer and create like an artist — whether I’m sculpting a character, boarding a sequence, or dimensioning a part for production.",
        "On the creative side I work across <strong>3D design, sculpting and animation</strong> as well as <strong>2D illustration, storyboarding and animation</strong>. On the technical side I bring <strong>SolidWorks, AutoCAD</strong> and solid mechanical design fundamentals to build things that actually work.",
    ],
    "creative": {"label": "🎨 Creative", "sub": "Vision & storytelling"},
    "technical": {"label": "⚙️ Technical", "sub": "Precision & function"},
    "cta": {"text": "Let’s work together", "url": "#contact"},
}


# ============================================================
# SKILLS
# ============================================================
# Skill percentages are presentation values, not formal test scores.
# Change or remove them depending on how you want to represent proficiency.

SKILLS = [
    {
        "category": "Creative",
        "items": [
            {"name": "3D Modeling & Sculpting", "level": 95},
            {"name": "3D Animation & Rigging", "level": 88},
            {"name": "2D Illustration & Concept", "level": 92},
            {"name": "Storyboarding", "level": 85},
            {"name": "2D Animation", "level": 83},
        ],
        "tools": ["🧊 Blender", "🎺 ZBrush", "🎨 Substance", "✏️ Photoshop", "🖌️ Procreate", "🎬 After Effects"],
    },
    {
        "category": "Engineering",
        "items": [
            {"name": "SolidWorks", "level": 90},
            {"name": "AutoCAD", "level": 88},
            {"name": "Mechanical Design", "level": 92},
            {"name": "Design for Manufacture", "level": 82},
            {"name": "Technical Drawing / GD&T", "level": 85},
        ],
        "tools": ["📐 SolidWorks", "📈 AutoCAD", "🔧 Fusion 360", "🖨️ 3D Printing", "📊 MATLAB"],
    },
]


# ============================================================
# SERVICES
# ============================================================

SERVICES = [
    {
        "number": "01",
        "title": "3D Modeling & Sculpting",
        "description": "Characters, props, hard-surface and product models — game-ready or high-poly for cinematics and 3D print.",
    },
    {
        "number": "02",
        "title": "3D Animation",
        "description": "Rigging, character performance and product motion for film, ads, explainers and real-time.",
    },
    {
        "number": "03",
        "title": "Illustration & Concept Art",
        "description": "Editorial, character and environment illustration plus concept art to define a project’s look.",
    },
    {
        "number": "04",
        "title": "Storyboarding & 2D Animation",
        "description": "From boards and animatics to finished frame-by-frame or rigged 2D animation.",
    },
    {
        "number": "05",
        "title": "Mechanical / Product Design",
        "description": "Concept to CAD in SolidWorks & AutoCAD — parametric parts, assemblies, drawings and DFM.",
    },
    {
        "number": "06",
        "title": "Art + Engineering Consulting",
        "description": "Design that is both beautiful and buildable — bridging creative direction and manufacturing reality.",
    },
]


# ============================================================
# EXPERIENCE
# ============================================================
# Optional for now. Add entries when you want the section displayed.

EXPERIENCE = [
    # {
    #     "role": "Job Title",
    #     "organization": "Company / Organization",
    #     "period": "2025 — Present",
    #     "description": "Short description of the role.",
    #     "highlights": ["Achievement or responsibility", "Another achievement"],
    # },
]


# ============================================================
# EDUCATION
# ============================================================

EDUCATION = [
    {
        "qualification": "B.Eng. Mechanical Engineering",
        "institution": "Institution Name",
        "period": "Year — Year",
        "description": "Mechanical engineering education supporting the technical side of the portfolio.",
    },
]


# ============================================================
# SOCIALS
# ============================================================

SOCIALS = [
    {"name": "ArtStation", "url": "#"},
    {"name": "Instagram", "url": "#"},
    {"name": "LinkedIn", "url": "#"},
    {"name": "YouTube", "url": "#"},
    {"name": "Behance", "url": "#"},
]


# ============================================================
# CONTACT
# ============================================================

CONTACT = {
    "title": "Let’s create\nsomething great.",
    "description": (
        "Have a project in mind — a model, an animation, an illustration set "
        "or a part that needs designing? Reach out and let’s talk."
    ),
    "email": SITE["email"],
    "phone": SITE["phone"],
    "location": SITE["location"],
    "form": {
        "name_label": "Your name",
        "email_label": "Your email",
        "subject_label": "Project type (3D, 2D, CAD…)",
        "message_label": "Tell me about your project…",
        "submit_text": "Send message →",
    },
}
