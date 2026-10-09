SITE = {
    "name": "STUDIO/NAME",
    "title": "Portfolio — 3D & 2D Artist",
    "description": "3D and 2D art portfolio featuring modeling, sculpting, animation, illustration, concept art, and storyboarding.",
    "email": "hello@example.com",
    "phone": "+00 000 000 000",
    "location": "Available worldwide · Remote",
    "availability": "Available for freelance & collaborations",
    "footer_name": "Your Name",
}

HERO = {
    "heading_html": 'I create in <span class="stroke">3D</span> & <span class="accent">2D</span> —<br>built for visual storytelling.',
    "subheading": "A visual artist working across 3D modeling, sculpting, animation, illustration, concept art, and storyboarding to turn ideas into polished visual work.",
    "primary_text": "View my work →",
    "secondary_text": "Start a project",
    "stats": [
        {"number": "3D", "label": "Modeling & animation"},
        {"number": "2D", "label": "Art & animation"},
        {"number": "2", "label": "Core disciplines"},
    ],
}

DISCIPLINES = [
    {
        "icon": "🧊",
        "title": "3D Art & Animation",
        "description": "Modeling, sculpting, texturing, rigging, and animation for characters, props, environments, products, and visual storytelling.",
        "tags": ["Modeling", "Sculpting", "Texturing", "Rigging", "3D Animation"],
    },
    {
        "icon": "✏️",
        "title": "2D Art & Animation",
        "description": "Illustration, concept art, storyboarding, and 2D animation for developing ideas, defining visual direction, and telling stories.",
        "tags": ["Illustration", "Concept Art", "Storyboarding", "2D Animation"],
    },
]

# Only two portfolio filters are used: 3D and 2D.
PORTFOLIO_CATEGORIES = {
    "3d": "3D",
    "2d": "2D",
}

# Put project images in static/images/3d/ or static/images/2d/.
# If image is empty, the gradient is used as the placeholder.
WORKS = [
    {
        "title": "Creature Bust",
        "slug": "creature-bust",
        "category": "3d",
        "description": "Character sculpt developed as a detailed 3D study.",
        "tools": ["Blender", "ZBrush"],
        "skills": ["Sculpting", "Character Art"],
        "image": "",
        "gradient": ["#ff5c38", "#a56bff"],
        "featured": True,
        "links": {"project": "", "demo": ""},
    },
    {
        "title": "Sci-Fi Prop",
        "slug": "sci-fi-prop",
        "category": "3d",
        "description": "Hard-surface prop designed with a focus on form, detail, and presentation.",
        "tools": ["Blender", "Substance 3D"],
        "skills": ["Hard Surface", "Texturing"],
        "image": "",
        "gradient": ["#38b6ff", "#a56bff"],
        "featured": True,
        "links": {"project": "", "demo": ""},
    },
    {
        "title": "Character Walk Cycle",
        "slug": "character-walk-cycle",
        "category": "3d",
        "description": "Character animation study focused on movement, timing, and performance.",
        "tools": ["Blender"],
        "skills": ["Rigging", "3D Animation"],
        "image": "",
        "gradient": ["#a56bff", "#ff5c38"],
        "featured": False,
        "links": {"project": "", "demo": ""},
    },
    {
        "title": "Stylized Environment",
        "slug": "stylized-environment",
        "category": "3d",
        "description": "Stylized environment created to explore composition, modeling, materials, and atmosphere.",
        "tools": ["Blender", "Substance 3D"],
        "skills": ["Environment Art", "Materials"],
        "image": "",
        "gradient": ["#3ddc84", "#38b6ff"],
        "featured": False,
        "links": {"project": "", "demo": ""},
    },
    {
        "title": "Editorial Illustration",
        "slug": "editorial-illustration",
        "category": "2d",
        "description": "Illustration developed around a clear visual concept and editorial composition.",
        "tools": ["Photoshop", "Procreate"],
        "skills": ["Illustration", "Composition"],
        "image": "",
        "gradient": ["#ff5c38", "#ffb038"],
        "featured": True,
        "links": {"project": "", "demo": ""},
    },
    {
        "title": "Concept Character Sheet",
        "slug": "concept-character-sheet",
        "category": "2d",
        "description": "Character exploration showing shape language, design variations, and visual direction.",
        "tools": ["Photoshop", "Procreate"],
        "skills": ["Concept Art", "Character Design"],
        "image": "",
        "gradient": ["#ff5c38", "#a56bff"],
        "featured": False,
        "links": {"project": "", "demo": ""},
    },
    {
        "title": "Short Film Storyboard",
        "slug": "short-film-storyboard",
        "category": "2d",
        "description": "Storyboard sequence developed to communicate shots, composition, action, and pacing.",
        "tools": ["Photoshop", "Storyboard software"],
        "skills": ["Storyboarding", "Visual Development"],
        "image": "",
        "gradient": ["#38b6ff", "#3ddc84"],
        "featured": False,
        "links": {"project": "", "demo": ""},
    },
    {
        "title": "2D Animated Explainer",
        "slug": "2d-animated-explainer",
        "category": "2d",
        "description": "Short 2D animation focused on clear visual communication and motion.",
        "tools": ["After Effects", "Photoshop"],
        "skills": ["2D Animation", "Motion Design"],
        "image": "",
        "gradient": ["#a56bff", "#38b6ff"],
        "featured": False,
        "links": {"project": "", "demo": ""},
    },
]

ABOUT = {
    "title": "Two disciplines, one visual language",
    "paragraphs": [
        "This portfolio brings together <strong>3D and 2D visual work</strong>, covering modeling, sculpting, animation, illustration, concept art, and storyboarding.",
        "The focus is on creating clear, polished visuals that communicate an idea — from an individual character or prop to a complete sequence or visual concept.",
    ],
    "creative_label": "🎨 3D",
    "creative_sub": "Form & dimension",
    "technical_label": "✏️ 2D",
    "technical_sub": "Line & storytelling",
}

SKILLS = {
    "3d": [
        ("3D Modeling", 95),
        ("Sculpting", 90),
        ("Texturing", 85),
        ("Rigging", 80),
        ("3D Animation", 88),
    ],
    "3d_tools": ["🧊 Blender", "🎺 ZBrush", "🎨 Substance 3D"],
    "2d": [
        ("Illustration", 92),
        ("Concept Art", 90),
        ("Storyboarding", 85),
        ("2D Animation", 83),
        ("Motion Design", 80),
    ],
    "2d_tools": ["✏️ Photoshop", "🖌️ Procreate", "🎬 After Effects"],
}

SERVICES = [
    ("01", "3D Modeling & Sculpting", "Characters, props, environments, and product models from initial forms to polished final assets."),
    ("02", "3D Animation", "Rigging, character movement, product motion, and animation for visual storytelling."),
    ("03", "Illustration & Concept Art", "Illustration and concept development for characters, environments, editorial work, and visual direction."),
    ("04", "Storyboarding & 2D Animation", "Boards, animatics, frame-by-frame animation, and motion work for communicating stories and ideas."),
]

SOCIALS = [
    ("ArtStation", "#"),
    ("Instagram", "#"),
    ("YouTube", "#"),
    ("Behance", "#"),
]
