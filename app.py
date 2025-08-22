# app.py
import streamlit as st
import importlib.util
import os
from pathlib import Path
import base64
# Clear all cached data
st.cache_data.clear()


# Read GIF and encode to base64
with open("ss.png", "rb") as f:
    gif_bytes = f.read()
b64_gif = base64.b64encode(gif_bytes).decode()

def create_image_text_layout(image_path=None, text_content=None, layout="full", image_position="left"):
    """Reusable layout for image + text blocks"""
    if layout == "full":
        if image_path:
            st.image(image_path, use_container_width=True)
        if text_content:
            st.markdown(text_content, unsafe_allow_html=True)
    elif layout == "side":
        if image_position == "left":
            col1, col2 = st.columns([1, 2])
        else:
            col1, col2 = st.columns([2, 1])
        with col1:
            if image_position == "left" and image_path:
                st.image(image_path, use_container_width=True)
            elif image_position == "right" and text_content:
                st.markdown(text_content, unsafe_allow_html=True)
        with col2:
            if image_position == "left" and text_content:
                st.markdown(text_content, unsafe_allow_html=True)
            elif image_position == "right" and image_path:
                st.image(image_path, use_container_width=True)


def load_chapter_content(chapter_num):
    """Load content from chapter file"""
    try:
        chapter_file = f"chapter{chapter_num}.py"
        if os.path.exists(chapter_file):
            spec = importlib.util.spec_from_file_location(f"chapter{chapter_num}", chapter_file)
            if spec is not None and spec.loader is not None:
                chapter_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(chapter_module)
                return chapter_module
        return None
    except Exception:
        return None


def display_chapter_content(chapter_module, chapter_num):
    """Display chapter content with custom layouts if available"""
    if chapter_module is None:
        st.markdown(f'<div class="justified-text">Chapter {chapter_num} content not found.</div>', unsafe_allow_html=True)
        return
    try:
        if hasattr(chapter_module, 'display_content'):
            chapter_module.display_content()
        elif hasattr(chapter_module, 'get_content'):
            content = chapter_module.get_content()
            st.markdown(f'<div class="justified-text">{content}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="justified-text">No content available for Chapter {chapter_num}.</div>', unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f'<div class="justified-text">Error displaying Chapter {chapter_num}: {str(e)}</div>', unsafe_allow_html=True)


def main():
    # Page configuration
    st.set_page_config(page_title="Supercalifragilisticexpialidocious", page_icon="💀", layout="wide")

    # Put a top anchor so #top works
    st.markdown('<div id="top"></div>', unsafe_allow_html=True)

    # -----------------------
    # Handle nav query param and session state
    # -----------------------
    if "selected_chapter" not in st.session_state:
        st.session_state.selected_chapter = 1

    params = st.query_params
    nav = params.get("nav")
    if nav:
        if nav == "prev" and st.session_state.selected_chapter > 1:
            st.session_state.selected_chapter -= 1
        elif nav == "next" and st.session_state.selected_chapter < 11:
            st.session_state.selected_chapter += 1
        # clear query and rerun so it doesn't trigger again
        st.query_params.clear()
        st.rerun()

    # -----------------------
    # Sidebar styling + nav
    # -----------------------
    # Load PNG and convert to base64
    with open("skull2.png", "rb") as f:
        img_bytes = f.read()
    b64_cursor = base64.b64encode(img_bytes).decode()

    # Inject CSS
    # Inject CSS
    st.markdown(f"""
    <style>
    /* Apply custom cursor everywhere */
    *, body, html {{
        cursor: url("data:image/png;base64,{b64_cursor}") 16 16, auto !important;
    }}

    /* Force it even on interactive elements */
    button, a, div, span, input, textarea, [role="button"] {{
        cursor: url("data:image/png;base64,{b64_cursor}") 16 16, auto !important;
    }}
    </style>
    """, unsafe_allow_html=True)


    st.sidebar.markdown("""
    <style>
    [data-testid="stSidebar"] .stButton > button {
        justify-content: flex-start !important;
        text-align: left !important;
                        
    }
    [data-testid="stSidebar"] .stButton > button > div {
        width: 100%;
        text-align: left !important;
    }
    [data-testid="stSidebar"] .stButton > button[kind="primary"]{
        background: #0D0B1A !important;
        color: #e7b66c !important;
        border: 2px solid #e7b66c !important;
                    
        
    }
    </style>
    """, unsafe_allow_html=True)


    st.markdown(
    """
    <style>
    /* Set sidebar width */
    [data-testid="stSidebar"] {
        width: 400px !important;  /* Change this to your desired width */
    }

    /* Optional: adjust main content margin when sidebar width changes */
    [data-testid="stMainContent"] {
        margin-left: 400px !important;  /* slightly larger than sidebar width */
    }
    </style>
    """,
    unsafe_allow_html=True
    )






    st.sidebar.image("sidebar2.gif", use_container_width=True)

    chapter_names = {
        1: "When Tahir Found Malik, Chaos Found Me",
        2: "Anger Has a Name: Wahid",
        3: "The Gentle Entry of Karishma",
        4: "When Destiny Chose Four Souls to Meet",
        5: "Behind the Cool Mask",
        6: "The Truth Hunt Begins",
        7: "Goodbye Malik",
        8: "The Emotional Trap",
        9: "The Spark Against Wahid",
        10: "The Spark Against Karishma",
        11: "The Puppeteer's Confession"
    }

    for i in range(1, 12):
        btn_type = "primary" if i == st.session_state.selected_chapter else "secondary"
        if st.sidebar.button(
            f"Chapter {i}: {chapter_names[i]}",
            key=f"chapter_{i}",
            use_container_width=True,
            type=btn_type,
        ):
            st.session_state.selected_chapter = i
            st.rerun()


    # -----------------------
    # Title + fonts
    # -----------------------
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=New+Rocker&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Beth+Ellen&display=swap');

        .stApp h1 {
            font-family: 'New Rocker', cursive !important;
            font-size: 100px !important;
            color: #dca65b !important;
            text-align: center !important;
            letter-spacing: 2px !important;
        }
        p { 
            font-size: 18px !important;
            line-height: 1.6 !important;
            text-align: justify !important;
                
            color: oldlace;
        }
        .beth {
            font-family: 'Beth Ellen', cursive !important;
            font-size: 20px;
            text-align: center;
            color: oldlace !important;
            margin-top: 0.2em;
        }

        /* Smooth anchor scrolling */
        html {
            scroll-behavior: smooth !important;
        }

        /* -------- Responsive font sizes -------- */
        @media (max-width: 768px) {   /* tablets & small devices */
            .stApp h1 {
                font-size: 74px !important;
            }
            .beth {
                font-size: 18px !important;
            }
        }

        @media (max-width: 480px) {   /* mobile phones */
            .stApp h1 {
                font-size: 74px !important;
            }

            .beth {
                font-size: 16px !important;
            }
        }
        </style>
    """, unsafe_allow_html=True)


    st.title("Supercalifragilisticexpialidocious")
    st.markdown("<div class='beth'>- Danjin Master</div>", unsafe_allow_html=True)

    # -----------------------
    # Load & show chapter
    # -----------------------
    chapter_module = load_chapter_content(st.session_state.selected_chapter)
    display_chapter_content(chapter_module, st.session_state.selected_chapter)


    col1, col2 = st.columns([1, 1])

    with col1:
        # inner columns: button sits in the left-most sliver
        prev_col, _ = st.columns([3, 2])
        with prev_col:
            if st.session_state.get("selected_chapter", 1) > 1:
                if st.button("◀ Previous Chapter", key="prev_btn"):
                    st.query_params["nav"] = "prev"
                    st.rerun()

    with col2:
        # inner columns: right-most sliver holds the button
        _, next_col = st.columns([3, 2])
        with next_col:
            if st.session_state.get("selected_chapter", 1) < 11:
                if st.button("Next Chapter ▶", key="next_btn"):
                    st.query_params["nav"] = "next"
                    st.rerun()


    
    # -----------------------
    # Review Form
    # -----------------------

    st.markdown("""
    <style>
    .review-form {
        border: 2px solid #1E90FF; /* Blue border */
        border-radius: 10px;
        padding: 20px;
        background-color: #f9f9f9; /* Light background */
    }
    </style>
    """, unsafe_allow_html=True)


    st.markdown("## Leave a Review")
    with st.form("review_form"):
        name = st.text_input("Your Name")
        review = st.text_area("Your Review about this story")
        submitted = st.form_submit_button("Submit Review")

        if submitted:
            if name.strip() == "" or review.strip() == "":
                st.error("Please fill out both fields before submitting.")
            else:
                from google_sheets import add_review
                add_review(name, review, st.session_state.selected_chapter)
                st.success("✅ Thank you! Your review has been saved.")



    st.markdown("""
    <style>
    html {
        scroll-behavior: smooth; /* enables smooth scroll */
    }
    html, body {
        scroll-behavior: smooth;
    }

    .scroll-buttons {
        position: fixed;
        bottom: 20px;
        right: 20px;
        display: flex;
        flex-direction: column;
        gap: 10px;
        z-index: 9999;
    }
    .scroll-btn {
        display:inline-flex;
        align-items:center;
        justify-content:center;
        width:48px;
        height:48px;
        border-radius:50%;
        background:#0D0B1A;
        color:#e7b66c !important;
        border:2px solid #e7b66c;
        text-decoration:none !important;
        transition: all 0.3s ease; /* smooth hover transition */
    }
    .scroll-btn:hover {
        background:#e7b66c !important;
        color:#0D0B1A !important;
    }
    .scroll-btn svg {
        width:24px;
        height:24px;
        fill:currentColor;
    }
    </style>

    <!-- invisible anchors for scroll target -->
    <div id="top"></div>

    <div class="scroll-buttons" aria-hidden="true">
        <a class="scroll-btn" href="#top" title="Scroll to top">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path d="M12 4l-8 8h6v8h4v-8h6z"/>
            </svg>
        </a>
        <a class="scroll-btn" href="#bottom" title="Scroll to bottom">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path d="M12 20l8-8h-6V4h-4v8H4z"/>
            </svg>
        </a>
    </div>

    <!-- target for bottom scroll -->
    <div id="bottom"></div>
    """, unsafe_allow_html=True)

    # Sticky GIF at top-right, hidden on mobile
    st.markdown(f"""
    <style>
    .top-right-gif {{
        position: fixed;
        top: 70px;
        right: -3px;
        z-index: 1000;
        border: 2px solid #dca65b ;
        border-radius: 2px;
    }}

    @media (max-width: 768px) {{
        .top-right-gif {{
            display: none !important;
        }}
    }}
    </style>
    <div class="top-right-gif">
        <img src="data:image/gif;base64,{b64_gif}" width="300">
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
