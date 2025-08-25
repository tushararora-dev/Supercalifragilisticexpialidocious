import streamlit as st
from app import create_image_text_layout   # reuse function from main.py

def display_content():

    st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=UnifrakturCook:wght@700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Beth+Ellen&display=swap');
    h2 {
        font-family: 'UnifrakturCook', cursive !important;
        font-size: 48px;
        text-align: center;
        color: #e7b66c !important;
    }
    p, li { 
        font-size: 18px !important;
        # line-height: 1.6 !important;
        text-align: justify !important;
        color: oldlace;
    }

    table {
        border-collapse: collapse;
        width: 100%;
    }

    td {
        border: 2px solid #444 !important;
        padding: 5px;
        font-size: 16Fpx !important;
        line-height: 1.2 !important;
        text-align: justify !important;
        color: oldlace;
        background-color: #6969691f; /* dark background to contrast oldlace */
    }


    .beth1 {
            font-family: 'Beth Ellen', cursive !important; /* <-- use Beth Ellen (imported) */
            font-size: 22px;
            color: oldlace !important;
            text-align: center !important;
            margin-top: 0.2em;
            color: dimgray !important;
        }

    </style>
    """,
    unsafe_allow_html=True
    )
    create_image_text_layout("attached_assets/generated_images/chap3main.jpg", layout="full")


    text0 = """
    <h2>Chapter 3: The Gentle Entry of Karishma</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")


    text1 = """
    <p>
    Sham ka waqt tha. Shuruat hoti hai ek lazy evening se, jab main apne dost <span style="color:#FF5733;">Buraat</span> ke saath Discord ke voice channel par aaram se chill kar raha tha. Background mein halki keyboard ki tapping, mic ke pop, aur hum dono bas chilling mode mein the. casually baat kar rahe the — Buraat apne usual sarcastic mood me tha, thodi masti, mahol relaxed tha.

    Bina kisi warning ke, ek random entry hoti hai ek ladki ki — Karishma. Profile pic: ek French chemist aur <span style="color:#FF5733;">physicist scientist</span>, specs pehne hue. VC mein entry maar gayi… Main bas relax mode mein tha. Maine poocha: “Kaun aaya?” Uske aate hi, Buraat aur Karishma ke beech lafde ki bijli gir padi. Bas… us ek line ne hawa badal di. Idhar-udhar comments, “pata nahi kya kya” insults — <span style="color:#FF5733;">Mongolpuri</span> se leke random dialogues ka udaan. Dono ek dusre ko random jagah, random naam se bula rahe the. Mujhe laga bas thoda fun banega. Hasi bhi aayi. Lekin kuch hi minute me baat badh gayi. 2-3 lines ke baad mahol garam — galiyan, tikhiyan baatein…
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap31.jpg", text1, layout="side", image_position="right")




    text2 = """
    <p>
    Shock tab laga jab Buraat ne apna trump card nikala — server ka “verdict” room. Us din usne backup call kiya. Ye ek <span style="color:#FF5733;">psychological move</span>  tha jo main ache se jaanta hoon — "Control the environment, control the outcome." Jab tum kisi ko apne defined rules ke space mein kheench lete ho, tum game ka direction decide karte ho. Buraat ne exactly wahi kiya. Usne Karishma ko “online jail” — yani server ke <span style="color:#FF5733;">verdict room</span> — mein bhej diya. Us din pura anti-Bihari group ka sir sharam se jhuk gaya. Mujhe regret feel hua. Socha, agar faisla hum lete to shayad yeh kahani kabhi shuru hi na hoti. Haan, agar waisa hota to bas punishment milta — maut ya dand nahi.

    Maut mritua hai, lekin ab usko dand milega. Aur Buraat jaise logon ki wajah se mujhe bhi <span style="color:#FF5733;">maafi</span> mangni padi. Kabhi-kabhi, jo log zindagi me entry marte hain… wo ek kahani ka plot twist ban jaate hain. "Ek random entry sirf ek new member nahi… ek poora plot twist hota hai."
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap32.jpg", text2, layout="side", image_position="left")



    text3 = """
    <p>
    Thode din baad, Karishma aur uski saheli VC mein aayi — pure roasting ke mood mein. Lekin hamara comeback unke liye zyada tha — meri <span style="color:#FF5733;">bharpur awaaz</span> aur neech soch kaafi thi. Meri awaaz deep thi, soch thodi dark… comeback unke liye too much tha. Us din hamare saath ek aur banda tha — Raqsaan. Karishma ke kehne par pata chala, vo piche hi pada hua tha. Wahi se baatein shuru ho gayi. Karishma ne call par aake sab kuch bataya… aur ekdum sab pause ho gaya.

    Phir ek din, bina kuch bole, usne apna chehra dikhaya. Main tabhi samajh gaya — yeh ek confidence test tha. Reaction hi test ka part tha. Bina shabd ke mystery create karna ek <span style="color:#FF5733;">psychological trick</span> hai — curiosity badhane ka ek proven tareeka. Samne wale ke dimaag me 10 sawal daal do, aur control tumhare paas hota hai.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap33.jpg", text3, layout="side", image_position="right")



    text4 = """
    <p>
    Par bharosa karna mushkil tha. Maine poocha bhi nahi ki yeh real hai ya fake, kyunki mujhe lagta tha vo chahti thi main confuse rahun. Itna kamzor khiladi main nahi. Jab tum apna <span style="color:#FF5733;">motive unclear</span> rakhte ho, samne wale ki curiosity naturally badh jaati hai. Lekin maine us game mein jump nahi kiya. Is game mein patience jeetata hai, reaction nahi.
    </p>
    """
    create_image_text_layout(text_content=text4, layout="full")



    text5 = """
    <p>
    Us time tak hum “online jail” ka process almost chhod chuke the. Bulk roast ka era shaant ho chuka tha. Tabhi ek din Karishma ka message aaya — “<span style="color:#FF5733;">HELP</span>.” Maine pucha, “Kya hua?” Usne kaha, “Kuch lafda ho gaya.”

    Jab tak main reply deta, matter solve ho chuka tha. Lekin principle simple hai — ek baar <span style="color:#FF5733;">contract </span>leliya, to le liya. Chhota ho ya bada, finish karna padta hai.

    Main aur 6-7 log seedha us bande ke server par gaye — full raid mode mein. Pata chala, uska connection upar tak tha. Koi baat nahi… humne apna kaam kiya, aur result — humein us server se <span style="color:#FF5733;">kick</span> kar diya gaya. Jaise kisi kaafir ko apne mulk se nikal dete hain.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap34.jpg", text5, layout="side", image_position="left")



    text6 = """
    <p>
    "<span style="color:#FF5733;">Kick is a win</span>." Agar hum jail mein chhod dete — matlab “server mute” — to unki jeet hoti. Kick karke to humne unka naam hamesha ke liye likh diya. Main sirf hasa: “<span style="color:#FF5733;">Kick matlab jeet</span>. Kyunki jail me dalte to unki authority bachi rehti. Kick karna unka defeat accept karna hai.”
    </p>
    """
    create_image_text_layout(text_content=text6, layout="full")




    text7 = """
    <p>
    Is event ke baad uska naam anti-Bihari group mein “<span style="color:#FF5733;">Contractor</span>” pad gaya Aur main dekhna chahta tha… isme dum kitna hai. Lekin mujhe curiosity thi — “Isme potential hai… ya nahi?”
    Ek din pata chala ki vo apni 3 ladkiyon ki team ke saath chhote level par wahi kaam kar rahi hai jo hum chhod chuke the — bulk roast. Lekin ek difference tha. Jo hum karte the, vo trauma level ka hota tha. Inka kaam starting stage pe tha — zyada impact nahi. <span style="color:#FF5733;">Execution mein flaws</span> the… jaise nailcutter se ped kaatne ka try.
    <br> <br>
    Main ne usko tips di aur roasting ke <span style="color:#FF5733;">golden rules</span> samjhaye: “Dekho, roasting mein jeet wahi sakta hai jo ya to emotionally strong ho, ya jiske contacts ho. Agar opponent tumhe chidhata hai aur tum react kar gaye… tum haar gaye.”
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap35.jpg", text7, layout="side", image_position="right")


    text71 = """
        <ul>
        <li><span style="color:#FF5733;">Emotionally Strong Bano</span> : Online roast mein jo emotionally strong hai, wahi jeet sakta hai.
    Opponent jitna bhi provoke kare, gussa mat karo. Chill raho. Punchline calm ya hasi ke saath do.
    Agar tum gusse me chillaoge aur opponent neutral tone me reply dega, audience uske saath ho jayegi.</li>
        <li><span style="color:#FF5733;">OBS Tricks & Tactical Creativity</span> :
    Audience ko engage karo.
    Opponent ki hakikat dikhane ka mauka mile to lo — sharm induce karo.
    Punchline me soundboard, creative shayari ya instant meme use karo.
    Screen share karke opponent ka embarrassing truth dikhana — audience ka focus instantly tum pe le aata hai.
    Roast ka asli goal audience ka entertainment hai. Jeet unki hansi se hoti hai, tumhare punchline se nahi.</li>
    <li><span style="color:#FF5733;">Timing & Restraint</span>
    Patience rakho. Punchline tab maro jab zarurat ho.
    Agar right time pe hit karoge, impact double ho jaata hai.
    Galat time pe, sirf tumhara gussa dikhai dega.</li>
    </ul>
    """
    create_image_text_layout("attached_assets/generated_images/chap36.jpg", text71, layout="side", image_position="left")




    text8 = """
    <p>Main khud observe kar raha tha, aur soch raha tha:
    Ye ladki strong hai, aur sikhne ko ready hai. Confidence, patience, aur strategy — ye combination har battle jeetata hai.
    Karishma ke moves calm, calculated, aur audience ke nazar me <span style="color:#FF5733;">unbeatable</span> the.
    Emotionally strong rehna, strategy plan karna, aur audience grab karna hi jeet ke asli keys hain.</p>

    <table>
    <tr>
        <td> 1. Emotionally strong bano  <br>— gussa mat karo, punchline calm ya hasi ke saath do.</td>
        <td> 2. OBS ka use karo  <br>— opponent ki sachchai screen pe laa ke unko sharminda karo.</td>
        <td> 3. Audience ka attention lo  <br>— shayari, sound effects, ya surprise elements.</td>
    </tr>
    </table>

    """
    create_image_text_layout(text_content=text8, layout="full")


    text9 = """
    <p>
        Baad mein maine uske character ka deeper analysis kiya.
        Usme ego nahi tha — aur jisme ego nahi hota, unke <span style="color:#FF5733;">attention-seeking</span> hone ke chances hote hain.
        Attention-seekers insecure hote hain. Aur <span style="color:#FF5733;">insecure</span> log kabhi stable nahi hote — idhar-udhar bhatak kar apni tanhaayi chhupate rehte hain.
        Karishma bhi waise hi thi — jo kabhi ek jagah nahi rukti.
        Lekin wahi uski pehchan thi… aur shayad isi wajah se yeh kahani aage badhne wali thi. <br><br>
        Karishma mein ego nahi tha — aur ego jahan nahi hota, wahan chhote chhote openings milte hain.
        jisme <span style="color:#FF5733;">insecurity</span> hoti hai, aur wahi unka weak point hota hai.
        Woh apni loneliness ko mask karte hain, apne aap ko scatter karke.
        Real power aati hai <span style="color:#FF5733;">self-control</span> aur strategy se, na ki loudness aur gusse se.
        Confidence dikhana, curiosity create karna, aur audience ko control karna — yehi asli jeet hai, online ho ya real life.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap37.jpg", text9, layout="side", image_position="right")


    text10 = """
<table border="1" cellpadding="8" cellspacing="0" style="border-collapse: collapse; width: 100%;">
    <tbody>
        <tr>
            <td style="color:#FF5733;">Battle jeetne ke liye shor nahi, control chahiye:</td>
            <td>Punchline ka timing awaaz se bada hota hai. Jo banda gusse ko tame kar leta hai… chahe virtual ho ya real, har battlefield ka king hota hai.</td>
        </tr>
        <tr>
            <td style="color:#FF5733;">Game me jeetne ka secret simple hai:</td>
            <td>React mat karo, observe karo. Har move ka ek pattern hota hai, aur jo pattern read kar leta hai… vo kabhi harta nahi.</td>
        </tr>
        <tr>
            <td style="color:#FF5733;">Emotions tumhare soldier hai:</td>
            <td>Unhe discipline do, warna vo tumhara army tod denge.</td>
        </tr>
        <tr>
            <td style="color:#FF5733;">Battle me jeetne ke liye volume nahi, timing chahiye:</td>
            <td>Gussa nahi, control chahiye. Jo apne emotions ka master ban gaya… uska har battlefield pe raj hota hai.</td>
        </tr>
        <tr>
            <td style="color:#FF5733;">Game ka maza tab badh jaata hai:</td>
            <td>Jab player sochta hai ki vo tumhe control kar raha hai, aur tum uske saath game khel rahe hote ho.</td>
        </tr>
    </tbody>
</table>

    """
    create_image_text_layout("attached_assets/generated_images/chap38.jpg", text10, layout="side", image_position="left")






    create_image_text_layout("attached_assets/generated_images/chap3ban.jpg", layout="full")
    text111 = """
    <p> <div class='beth1'>A battle of words is not won by breaking the opponent, but by capturing the hearts of those who listen.
For the crowd does not follow rage, it follows reason wrapped in wit. - Danjin Master<br> <br>
    </p>

    """
    create_image_text_layout(text_content=text111, layout="full")
 