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
    create_image_text_layout("attached_assets/generated_images/chap6main.jpg", layout="full")


    text0 = """
    <h2>Chapter 6: Goodbye Malik</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")


    text1 = """
    <p>
    "Jab niyat saaf ho, toh har chaal ek teer ki tarah nishane par lagti hai." Main Malik aur Wahid ko hatane ka plan bana raha tha. Lekin har mastermind plan ke pehle ek question aata hai — <span style="color:#FF5733;">"Kya yeh sahi hai?"</span> 

    Mere dil ne poocha. Mere conscience ne doubt uthaya.
    Lekin us waqt ek awaaz aayi — <span style="color:#FF5733;">ek spiritual awaaz</span> , jaise nature khud mujhe guide kar rahi ho: "Jo tu soch raha hai, woh hoga. Tu sirf ek medium hai. Jo hone wala hai, woh hoke rahega."

    Mujhe samajh aaya — main karta nahi, main instrument hoon.
    Aur jab baat Karishma ki aati hai, jo mujhe <span style="color:#FF5733;">“Bada Bhai”</span>  kehti hai, toh mere liye uska safety first hai.
    Kisi bhi game me, sabse pehle weakest ya easiest target nahi chuna jata.
    Sabse close, sabse trusted, aur sabse deep rooted insaan ko todna padta hai — kyunki uske tootne se chain reaction hota hai.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap61.jpg", text1, layout="side", image_position="right")




    text2 = """
    <p>
    Malik, Karishma ka sabse close tha. Agar main directly uski harkate batata, Karishma shayad believe na karti — kyunki unka bond kaafi strong tha. Yahan ek psychological trick kaam aati hai:
    <span style="color:#FF5733;">Proof > Words</span> .
    Bina proof ke baat karna, apne image ko risk me dalna hai. Proof dikhana = instant trust + credibility.

    Malik ke saath kuch waqt spend kiya. Uski taarif ki. Har baat agree ki. Uska dosti ka illusion banaya. Ye  <span style="color:#FF5733;">mirroring technique</span> hai psychology me — jab tum kisi ki language, tone aur ideas mirror karte ho, toh woh samajhta hai ki tum uske side ho. Uske subconscious mind me tum “safe” ban jaate ho.

    Andar se mujhe gussa tha, lekin bahar se calm.
    Target ko comfortable karna tha, taaki woh apna guard down kare. Yahan main ek covert  <span style="color:#FF5733;">information extraction</span> mode me chala gaya. Mene recording start ki — aur Malik khud apni game reveal karne laga.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap62.jpg", text2, layout="side", image_position="left")





    text3 = """
    <p>
    Audio Content (Detailed Explanation):
    <table border="1" cellpadding="8" cellspacing="0">
    <tr><td><span style="color:#FF5733;">Character Analysis in Wrong Way</span> – Logon ke character ka analysis karke, galat tarike se manipulate karna.</td></tr>
    <tr><td><span style="color:#FF5733;">Lesson</span> – Kabhi apna character kisi aur ke haath me mat do.</td></tr>
    <tr><td><span style="color:#FF5733;">Future Planning</span> – Long term and short term game decide karna.</td></tr>
    <tr><td><span style="color:#FF5733;">Strategy Thinking</span> – A real manipulator plans months ahead.</td></tr>
    <tr><td><span style="color:#FF5733;">Sacrifice Advice</span> – “Sacrifice karo, par samne wale ko pata na chale.”</td></tr>
    <tr><td><span style="color:#FF5733;">Emotional Debt Creation</span> – Jab banda jaanta bhi nahi ki tumne sacrifice kiya, par tum indirectly uska mind shape kar rahe ho.</td></tr>
    <tr><td><span style="color:#FF5733;">One Wheel Analogy</span> – “Dono ek ek wheel pe hain, ek dooba toh dono doobenge.”</td></tr>
    <tr><td><span style="color:#FF5733;">Mutual Destruction Threat</span> – Ek manipulator ka safety net.</td></tr>
    </table>
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap63.jpg", text3, layout="side", image_position="right")



    text31 = """
    <p>
<table border="1" cellpadding="8" cellspacing="0">
  <tr><td><span style="color:#FF5733;">Fake Stories to Gain Trust</span> – Bar bar ek jhooth repeat karke usko sach banane ka illusion create karna.</td></tr>
  <tr><td><span style="color:#FF5733;">Illusion of Truth Effect</span> – Psychology Fact: Human brain repetition ko truth samajhne lagta hai.</td></tr>
  <tr><td><span style="color:#FF5733;">Manipulator VP Concept</span> – Manipulator kabhi front me nahi aata.</td></tr>
  <tr><td><span style="color:#FF5733;">Covert Leadership</span> – Ye ek covert leadership style hai — power me rehna, par spotlight se door.</td></tr>
  <tr><td><span style="color:#FF5733;">Long Game Listening & Persona Switching</span> – Lambi Game Plan – “Achha listener bano, multi personality Disorder chahiye.”</td></tr>
  <tr><td><span style="color:#FF5733;">Social Engineering</span> – Ye classic social engineering hai — har group me alag persona rakhna.</td></tr>
  <tr><td><span style="color:#FF5733;">Confusion Tactic</span> – Relationship me aao, phir piche hat jao.</td></tr>
  <tr><td><span style="color:#FF5733;">Emotional Push-Pull</span> – Emotional push-pull game — addictive hota hai.</td></tr>
</table>
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap64.jpg", text31, layout="side", image_position="left")

    text4 = """
    <p>
Aur bahut kuch tha jo main yahan nahi bata sakta. Malik ke paas mind games ka arsenal tha.
Mere paas emotions ka. "Mind ko confuse kiya ja sakta hai, par dil se jo connect ho jaaye, usse todna mushkil hai."

Main <span style="color:#FF5733;">“Dumb Game”</span> ka master tha — logon ko dikhana ki mujhe kuch samajh nahi aata.
Yeh ek reverse psychology shield tha — jab tum underestimated hote ho, tum sabse dangerous hote ho. Recording ka waqt aa gaya.
Sabko dikhaya — saath me <span style="color:#FF5733;">Squid Game</span> ka reference diya:

<span style="color:#FF5733;">“Ye Malik front man hai, aur main Seong Gi-hun.”</span>  Jab analogy relatable hoti hai, to log instantly connect karte hain.
Malik unstable ho gaya — profile picture change, inconsistent behavior, and finally… block from multiple people.
    </p>
    """
    create_image_text_layout("attached_assets/generated_images/chap65.jpg", text4, layout="side", image_position="right")



    text5 = """
   Ek mastermind ko confuse karna hi uski sabse badi haar hoti hai.
Malik ka stability chala gaya. Uske paas ek hi option tha — <span style="color:#FF5733;">"Underground ho jaana."</span>
Aur maine uska game over kar diya.

Baad me pata chala — Malik ne kuch baatein nikalwane ke liye bada sacrifice kiya tha, even family photos share karke.
Yeh ek reminder tha ki manipulator apna personal life bhi ek chess piece bana leta hai. Kya maine sahi kiya?
Yes — kyunki:

<table border="1">
  <tr>
    <td>Karishma meri “sister” thi aur uske saath galat ho raha tha.</td>
  </tr>
  <tr>
    <td>Woh paise nikalne ka kaam secretly kar raha tha mere connections ke sath.</td>
  </tr>
  <tr>
    <td>Mujhe galat cheezon ka blame de raha tha.</td>
  </tr>
  <tr>
    <td>Usne mere 6 saal purane dost ki insult kiya.</td>
  </tr>
</table>

Mujhe yeh samajh aa gaya tha ki main sirf ek medium hoon.
Main sochta tha, aur cheezein waise hi hoti thi — effortless, jaise nature khud mere liye rasta bana rahi ho. <span style="color:#FF5733;">"Jab tumhara maksad shuddh ho, toh kaaynaat tumhare liye chaal chalti hai."</span> 
    """
    create_image_text_layout("attached_assets/generated_images/chap66.jpg", text5, layout="side", image_position="left")






    create_image_text_layout("attached_assets/generated_images/chap6ban.jpg", layout="full")
    text111 = """
    <p> <div class='beth1'>Proof is greater than words; trust and credibility come with evidence, not just claims. - Danjin Master<br> <br>
    </p>

    """
    create_image_text_layout(text_content=text111, layout="full")
 