# app.py
import streamlit as st
import importlib.util
import os
from pathlib import Path
import base64
# Clear all cached data
st.cache_data.clear()
import math

# Read GIF and encode to base64
with open("ssgif.gif", "rb") as f:
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


def display_home(chapter_names):

    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=UnifrakturCook:wght@700&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Beth+Ellen&display=swap');

        h2 {
            font-family: 'UnifrakturCook', cursive !important;
            font-size: 25px !important;
            color: #e7b66c !important;
        }

        /* Vignette effect for main image */
        .vignette-image {
            position: relative;
            width: 100%;
            # max-width: 100%;
            display: block;
            margin: 0 auto;
        }

        .vignette-image::after {
            content: "";
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            pointer-events: none;
            background: radial-gradient(circle, rgba(13,11,26,0) 60%, rgba(13,11,26,0.95) 100%);

        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Main image with vignette
    img_path = "attached_assets/generated_images/main.jpg"
    if os.path.exists(img_path):
        with open(img_path, "rb") as f:
            img_bytes = f.read()
            encoded = base64.b64encode(img_bytes).decode()
        st.markdown(
            f"""
            <div class="vignette-image">
                <img src="data:image/jpg;base64,{encoded}" style="width:100%; display:block;"/>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown("🛠️ Working on it...")

    st.markdown(" ## Chapters :")

    # ---------------------------
    # Chapter 1 (manual)
    # ---------------------------
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        img_path = "attached_assets/generated_images/chap1main.jpg"
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
        else:
            st.markdown("🛠️ Working on it...")

    with col2:
        st.markdown(" ## Chapter 1: When Tahir Found Malik, Chaos Found Me")
        st.markdown("Aaj jab main apni kahani likhne baitha hoon, to sabse pehla sawal mere dimag mein ghoom raha hai – “Akhir main Malik se mila hi kyun?” Aur jab mila… to meri zindagi ne ek naya rang le liya ...")

    with col3:
        st.markdown(
            '<a href="?chapter=1#top" target="_self" '
            'style="display:inline-block;padding:10px 14px;border-radius:8px;'
            'border:2px solid #e7b66c;color:oldlace;background:#0D0B1A;'
            'text-decoration:none;">Read More ▶</a>',
            unsafe_allow_html=True
        )

    # st.markdown("---")

    # ---------------------------
    # Chapter 2 (manual)
    # ---------------------------
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        img_path = "attached_assets/generated_images/chap2main.jpg"
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
        else:
            st.markdown("🛠️ Working on it...")

    with col2:
        st.markdown(" ## Chapter 2: Anger Has a Name – Wahid")

        st.markdown("Malik ke sath meri baat-chit chal hi rahi thi ki ek aur chehra meri zindagi me aaya – Wahid. Random voice channel me mulaqat hui thi. Pehle to friendly roast, halka-phulka mazaak, aur ...")

    with col3:
        st.markdown(
            '<a href="?chapter=2#top" target="_self" '
            'style="display:inline-block;padding:10px 14px;border-radius:8px;'
            'border:2px solid #e7b66c;color:oldlace;background:#0D0B1A;'
            'text-decoration:none;">Read More ▶</a>',
            unsafe_allow_html=True
        )

    # st.markdown("---")

        # ---------------------------
    # Chapter 3 (manual)
    # ---------------------------
    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        img_path = "attached_assets/generated_images/chap3main.jpg"
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
        else:
            st.markdown("🛠️ Working on it...")

    with col2:
        st.markdown(" ## Chapter 3: The Gentle Entry of Karishma")
        
        st.markdown("Working on it...")

    with col3:
        st.markdown(
            '<a href="?chapter=3#top" target="_self" '
            'style="display:inline-block;padding:10px 14px;border-radius:8px;'
            'border:2px solid #e7b66c;color:oldlace;background:#0D0B1A;'
            'text-decoration:none;">Read More ▶</a>',
            unsafe_allow_html=True
        )

    # # Chapter 4 (manual)
    # # ---------------------------
    # col1, col2, col3 = st.columns([1, 3, 1])

    # with col1:
    #     img_path = "attached_assets/generated_images/chap4main.jpg"
    #     if os.path.exists(img_path):
    #         st.image(img_path, use_container_width=True)
    #     else:
    #         st.markdown("🛠️ Working on it...")

    # with col2:
    #     st.markdown(" ## Chapter 4: When Destiny Chose Four Souls to Meet")
        
    #     st.markdown("Working on it...")

    # with col3:
    #     st.markdown(
    #         '<a href="?chapter=4#top" target="_self" '
    #         'style="display:inline-block;padding:10px 14px;border-radius:8px;'
    #         'border:2px solid #e7b66c;color:oldlace;background:#0D0B1A;'
    #         'text-decoration:none;">Read More ▶</a>',
    #         unsafe_allow_html=True
    #     )




    st.markdown("---")



def main():
    # Page configuration
    st.set_page_config(page_title="Supercalifragilisticexpialidocious", page_icon="💀", layout="wide")

    # Auto-scroll to top if viewing a chapter (not home)
    if st.session_state.get("selected_chapter") != "home":
        st.markdown("""
            <script>
            window.onload = function() {
                window.scrollTo({top: 0, behavior: "instant"});
            };
            </script>
        """, unsafe_allow_html=True)

    # Put a top anchor so #top works
    st.markdown('<div id="top"></div>', unsafe_allow_html=True)

    # -----------------------
    # Handle URL query params + session state
    # -----------------------
    if "selected_chapter" not in st.session_state:
        st.session_state.selected_chapter = "home"

    params = st.query_params

    # Deep-link: /?chapter=3 loads Chapter 3 from the top
    ch = params.get("chapter")
    if ch:
        try:
            ch_num = int(ch)
            if 1 <= ch_num <= 11:
                st.session_state.selected_chapter = ch_num
        except:
            pass  # ignore bad values

    # Keep your existing 'nav' handling if you still want it
    nav = params.get("nav")
    if nav and isinstance(st.session_state.selected_chapter, int):
        if nav == "prev" and st.session_state.selected_chapter > 1:
            st.session_state.selected_chapter -= 1
        elif nav == "next" and st.session_state.selected_chapter < 11:
            st.session_state.selected_chapter += 1
        st.query_params.clear()

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

    # -----------------------
    # Sidebar chapter links (real navigation)
    # -----------------------
    for i in range(1, 12):
        active = (i == st.session_state.selected_chapter)
        target = "_self"  # change to "_blank" if you want new tab
        base = "display:block;width:100%;padding:10px 12px;border-radius:10px;text-decoration:none;margin-bottom:8px;"
        if active:
            style = base + "background:#0D0B1A;color:oldlace;border:2px solid #e7b66c;"
        else:
            style = base + "background:transparent;color:oldlace;border:1px solid #444;"
        st.sidebar.markdown(
            f'<a href="?chapter={i}#top" target="{target}" style="{style}">Chapter {i}: {chapter_names[i]}</a>',
            unsafe_allow_html=True
        )



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
    st.markdown("<div class='beth'>- Danjin Master<br><br></div>", unsafe_allow_html=True)

    # -----------------------
    # Load & show chapter
    # -----------------------
    if st.session_state.selected_chapter == "home":
        display_home(chapter_names)
    else:
        chapter_num = int(st.session_state.selected_chapter)

        # Load & show chapter
        chapter_module = load_chapter_content(chapter_num)
        display_chapter_content(chapter_module, chapter_num)

        left, right = st.columns([1,1])
        with left:
            if chapter_num > 1:
                st.markdown(
                    f'<a href="?chapter={chapter_num-1}#top" target="_self" '
                    'style="display:inline-block;padding:10px 14px;border-radius:8px;'
                    'border:2px solid #e7b66c;color:oldlace;background:#0D0B1A;'
                    'text-decoration:none;">◀ Previous Chapter</a>',
                    unsafe_allow_html=True
                )
        with right:
            if chapter_num < 11:
                st.markdown(
                    f'<a href="?chapter={chapter_num+1}#top" target="_self" '
                    'style="display:inline-block;padding:10px 14px;border-radius:8px;float:right;'
                    'border:2px solid #e7b66c;color:oldlace;background:#0D0B1A;'
                    'text-decoration:none;">Next Chapter ▶</a>',
                    unsafe_allow_html=True
                )



    
    st.markdown(
        """
        <style>
        /* Wrap the whole form in a styled div */
        div[data-testid="stForm"] {
            border: 2px solid orange;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
        }
        # /* Form border */
        # div[data-testid="stForm"] {
        #     border: 2px solid orange;
        #     border-radius: 10px;
        #     padding: 20px;
        #     margin-bottom: 20px;
        # }

        # /* Submit button border */
        # div.stButton > button {
        #     border: 2px solid orange !important;
        #     border-radius: 8px;
        #     background-color: white;
        #     color: orange;
        #     font-weight: bold;
        #     padding: 0.5em 1em;
        # }

        # /* Hover effect */
        # div.stButton > button:hover {
        #     background-color: orange;
        #     color: white;
        # }
        </style>
        """,
        unsafe_allow_html=True
    )

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
        transition: all 0.3s ease;
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

    <div id="top"></div>

    <div class="scroll-buttons" aria-hidden="true">
        <a class="scroll-btn" href="?chapter=home#top" title="Go to Home">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path d="M3 9.5l9-7 9 7V20a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1V9.5z"/>
            </svg>
        </a>
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

    <div id="bottom"></div>
    """, unsafe_allow_html=True)




    # Sticky GIF at top-right, hidden on mobile
    st.markdown(f"""
    <style>
    .top-right-gif {{
        position: fixed;
        top: 20px;
        right: 0px;
        z-index: 1000;
        # border: 2px solid #dca65b ;
        # border-radius: 2px;
    }}

    @media (max-width: 768px) {{
        .top-right-gif {{
            display: none !important;
        }}
    }}
    </style>
    <div class="top-right-gif">
        <img src="data:image/gif;base64,{b64_gif}" width="200">
    </div>
    """, unsafe_allow_html=True)

    # Force scroll to top on each render
    st.markdown("""
        <script>
        window.addEventListener('load', function() {
            window.scrollTo(0, 0);
        });
        </script>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
