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
    create_image_text_layout("attached_assets/generated_images/chap8main.jpg", layout="full")


    text0 = """
    <h2>Chapter 8: The Spark Against Karishma</h2>
    """
    create_image_text_layout(text_content=text0, layout="full")



    text1 = """
Kehte hain: “<span style="color:#FF5733;">Sach wahi hota hai jo tumhe todta hai, aur jhoot wahi hota hai jo tumhe sambhalta hai.</span>”
“Sach badalta nahi, chahe tum usse maano ya ignore karo. Sach wahi rehta hai… bas tum usse kab dekhne ko ready hote ho, ye matter karta hai.” Is kahaani mein sach kya hai aur dhoka kya, ye kisi ko clear nahi tha. Har character apne angle se sahi tha, aur phir bhi sab galat lagte tha.

Ye kahani pyar ki nahi hai.
Ye kahani revenge ki bhi nahi hai.
Ye ek game hai — mind games, manipulation, aur ek aisi chaal jisme jeetne wala bhi haar jata hai.

Karishma gayab ho gayi.
Physically nahi… par emotionally. Apne aap ko lock kar liya tha. smile ke peeche ek andhera, har “I’m fine” ke peeche ek war.
Na phone uthana, na message ka reply. Sirf khamoshi.
Wahid VC calls pe idhar udhar ghoomta rehta. time pass krta, hasne ki acting, khud ki tanhai chhupane ki koshish.
<span style="color:#FF5733;">Par sabse badi baat?</span> main ending se gussa tha. Kyunki iss ending mein culprit ko saza hi nahi mili thi.
    """
    create_image_text_layout("attached_assets/generated_images/chap81.jpg", text1, layout="side", image_position="right")
  

    text11 = """
“<span style="color:#FF5733;">Game tabhi complete hota hai jab guilt ko punishment mile</span>. Warna sab adhoora hai.”
Maine force karta raha Wahid ko ki baat kar, call kar, aisa mat kar bla bla bla...
15 din ke silence ke baad maine khud phone uthaya aur Karishma ko call kiya.
“Kaise ho?”
Dusre side se ek halki si muskaan, “Recover mode mein hoon.”

Par awaaz ke peeche jo compulsion thi, wo mujhe clear sunayi di. Mujhe samajh aa gaya — ye dobara Wahid se baat karegi.
Aur wahi hua. Maine usko vishwas dilaya:
“Last 15 din jo bhi calls tujhe aayi thi, sab maine hi karvayi thi. Sirf isliye, taaki tu akeli na feel kare.” The Spark Against Wahid hogya tha… Ab Karishma Ki Bari
Par pyaar andha hota hai. “<span style="color:#FF5733;">Ab mujhe us spark ko Karishma ke against turn karna tha</span>.
Mujhe pata tha ek din wo zaroor lautegi. Aur lautegi toh Wahid ke paas hi jayegi.
Meri planning shuru ho gayi.

    """
    create_image_text_layout(text_content=text11, layout="full")
    
  

    text2 = """
Ab samay aagaya tha iska khel khatam karne ka. Usse pehle Main khud se ek sawal puchta raha—kyun kar raha hoon main ye sab? Phir reasons samne aaye:

<table border="1" cellpadding="8" cellspacing="0">
  <tr>
    <td>Usne jhooth bola.</td>
    <td>Usne mere peeche burai ki, abuse kiya.</td>
  </tr>
  <tr>
    <td>Karishma ko mere khilaaf bhadkaya.</td>
    <td>Aur sabse bada – 6 saal purane dosti ko todne ki koshish ki.</td>
  </tr>
</table>

Bas… ye hi proofs kaafi the usko todne ke liye. To ab mere paas iski insecurities thi jo isko khatam kar sakti thi. Jo mujhe alag-alag sources se mili thi. Ab iska dhang se use karna tha. "<span style="color:#FF5733;">War jitne ke liye soldier nahi, bas sahi waqt pe sahi weapon chahiye.</span>" It's time—the spark against Karishma. To mujhe kuch move chalna tha taki ye vo dard hamesha yaad rakhe aur victim Karishma bane.
Isse hoga ki thoda sa dard hoga, connection tootega aur attachment bhi, phir sab theek ho jaayega.

Ye sab cheezein meri file mein likhi gayi insecurities thi.
Aur insecurities hi sabse bada weapon hoti hain. “Insaan ko maarna mushkil hai, par uski insecurity ko trigger karna sabse aasan.” Ab bas mujhe us weapon ko sahi waqt pe istemaal karna tha.

    """
    create_image_text_layout("attached_assets/generated_images/chap82.jpg", text2, layout="side", image_position="left")
  


    text22 = """
Maine apna forcefully task zyada bada diya, log preshaan ho jate hain jab tum unse baar-baar ek hi chiz karvao aur vo karte bhi nahi. To vohi hua. Maine apna sabse dangerous weapon use kiya—<span style="color:#FF5733;">forcefully tasking</span>.
Insaan ek hi cheez baar-baar karne ko bole to uska patience hil jaata hai. Wahid bhi hil gaya. Maine apna pressure tactics badhaya. Same cheez baar-baar push karna. Ek hi point repeat karna. Ye technique insaan ko mentally exhaust kar deti hai. Aur jaise expected tha, wahid preshan hone lage or us trap mein phans gaya.

<span style="color:#FF5733;">karma wapis aa hi jata hai</span>. Vo time aagaya tha… Ab dumb game, emotional game, forcefully game, sab khatam hone wala tha.
Phir usne ek nayi chaal chalne ki koshish ki — 6 saal purana dost se mil kar mujhe isolate karne ka try. lekin 6 saal purani dosti hai, nahi tod paya. Nothing is eternal, log badal hi jaate hain. Aur waise bhi nhi, koi jaan-bujhkar karta hai. I feel a little sad about it anyways.
    """
    create_image_text_layout(text_content=text22, layout="full")
   
  


    text3 = """
So itna forcefully act karne ke baad ek din mein soch raha tha, “<span style="color:#FF5733;">Kaash abhi ladai start ho</span> jaaye jab tak Karishma vapas nahi aati.”
Aur nature ne meri soch sun li. Ladai shuru ho gayi, starting usne kri. Jab ladai start hui

Aur wahi mera waqt tha. Maine uski insecurities pe war karna shuru kiya. ek-ek insecurity uske saamne fekni shuru ki. ek-ek line uski body me teer ki tarah ghus rahi thi.
Ek ek line, ek ek attack.
Meri saanse ruk gayi bolte bolte, par main nahi ruka. Jab bol raha tha to aisa lag raha tha ki khud <span style="color:#FF5733;">maut ka saudagar</span> hoon.

Wahid short-tempered tha. Uski ego fragile thi.
Jaise hi maine deep cut maarna shuru kiya, uske muh se bas ek hi cheez nikalti rahi:
“<span style="color:#FF5733;">Ye sab tujhe kisne bataya? Kaun bola?</span>” jo ek saas mein gali dene wala, jab uska time aaya, kisne bataya…

Ab bari thi, vo kya karega… Aur jo socha tha, vohi hua.
Uska andar ka dar bahar aa gaya.
Aur wahi meri jeet thi. Bomb phat gaya. Mujhe 16 tags aaye.
Ek bande mein himmat nahi thi akela face karne ki, toh wo gang lekar aaya.
    """
    create_image_text_layout("attached_assets/generated_images/chap83.jpg", text3, layout="side", image_position="right")
  

    text33 = """
Phir maine final blow maara—
maine ek line likhi jo uske liye zameen hilane jaisi thi:
“Ye lo tumhari ma-ma ka number. Ab ek aur tag aaya toh call seedha ghar pe aayegi. ”Bas. Khel khatam. Ping band. Main har jagah se block ho gaya. "
<span style="color:#FF5733;">Kabhi kabhi haar ke bhi jeet hoti hai.</span> Aur kabhi jeet ke baad sab tumhe villain banate hain.”
    """
    create_image_text_layout(text_content=text33, layout="full")
   

    text4 = """
Ab usne socha hoga kaun bataya usko—sabse easily guess usne kiya hoga, Karishma. 
 Wahid ke dimaag me sirf ek shak—Karishma. Kyunki connection main hi tha.
<span style="color:#FF5733;">Shadayantra aisa racha, execute aisa ki 100% successful raha. </span>Aur Jaise maine socha tha, Karishma wapas aayi aur Wahid se milne ki koshish ki.
Aur phir hua…
Boooooom.
Scene blast ho gaya.

Mujhe nahi pata unke beech kya hua, but main sure tha—meri planning ne pura ground hila diya tha.
Aur phir… Karishma ne ek line boli jo mere dimaag me ab tak register hai. Can't disclose.

Malik, Wahid, Karishma—teeno ko apna-apna karma mila.
Aur thoda bahut meri wajah se unko mental stress bhi mila.
"<span style="color:#FF5733;">Karma doesn’t need a weapon. It just needs patience. Aur patience… main hi hoon.</span>"
But kahani complex thi. Positive bhi tha, negative bhi. Decisions har waqt situation ke hisaab se.
Jo insecurities thi, unhe main yahan disclose nahi kar sakta—confidential reasons. 
    """
    create_image_text_layout("attached_assets/generated_images/chap84.jpg", text4, layout="side", image_position="left")
  


    text5 = """Main Tanjirō aur vo mere liye Nezuko (Demon Slayer).
Main chaahta toh Karishma ke saath bonding theek kar sakta tha.
Par maine decide kiya dheere-dheere hint se cheezon ko close karna hai. Aur fir mera bhi karma aaya.
Main block ho gaya. <span style="color:#FF5733;">Server se kick ho gaya</span>. Har jagah se erase kar diya gaya.

Sometimes, the people we like don’t like us back, and it’s painful, but there’s nothing we can do about it.
You don’t understand.
I do. I do understand.
I know what it’s like when someone doesn’t feel the same way about you. Is kahani ke baad mujhe ek baat samajh aayi.
Mere liye love ka matlab hai care + sukh dena <span style="color:#FF5733;">without expecting anything back.</span>

Aur If i love someone — chahe dosti ka, chahe insaan aur pet ka chahe blood relation, love in the sense of care, chahe kesa bhi ho—
Toh Main uskel iya monster, psycho ya murderer bhi ban sakta hoon agar <span style="color:#FF5733;">kisi ne uske saath bura kiya toh.
</span>
    """
    create_image_text_layout("attached_assets/generated_images/chap85.jpg", text5, layout="side", image_position="right")
  

    text66 = """
That’s why bahut log milne ka try karte hain, par nature apne aap hi unka alag kar deta hai. <span style="color:#FF5733;">Nature khud hi unko mujhse alag kar deta hai.</span> Shayad accha hi hota hai. Unko samajh nahi aata hoga main kaun hoon. Kya kar sakta hoon unke liye. Bas yehi hai, raste mein aayega nahi koi, agar aaya to sar par naya crime lgega.
    """
    create_image_text_layout(text_content=text66, layout="full")
   


    text6 = """
    Ab baari aati hai, ye kahani kitni sach hai. Mere likhne ya na likhne se sach to nahi badal jayega. Sach na tumko pata hai, na un logon ko jo mere alava is story ke characters the. <span style="color:#FF5733;">To sach kya hai?</span> 
<table border="1" cellpadding="8" cellspacing="0">
    <tr>
        <td>Kya main sabko dobara milwana chahta tha? ye story banakar!</td>
        <td>Kya main future mein bhi permanently is story ko close karna chahta hoon?</td>
    </tr>
    <tr>
        <td>Kya maine vohi likha hai jo log sochte hai, ya maine vo likha hai jo main hoon?</td>
        <td>Kya maine sahi kiya ya galat kiya?</td>
    </tr>
    <tr>
        <td>Ye galat-sahi kya hai? Kitni sachchai hai?</td>
        <td>Kya main aisa hoon bhi ya nahi?</td>
    </tr>
    <tr>
        <td>Kya main aisa hoon ya sirf dikhata hoon?</td>
        <td>Kya main villain banke sab theek karna chahta hu?</td>
    </tr>
    <tr>
        <td>Kya maine galat kiya ya sahi?</td>
        <td>Kya main saviour tha?</td>
    </tr>
</table>

    """
    create_image_text_layout("attached_assets/generated_images/chap86.jpg", text6, layout="side", image_position="left")
  
    text77 = """
    Aise bahut sare questions hain, par in questions se sachchai to nahi badlegi, aur sachchai vo koi nahi jaanta.
    So it’s the ending part, and at last, I texted her on birthday:
    <span style="color:#FF5733;">“Happy birthday Karishma, I hope your day will be Supercalifragilisticexpialidocious.”</span>

    It’s my last word, without hoping or expecting a reply. FULL STOP.
    """
    create_image_text_layout(text_content=text77, layout="full")
   


    create_image_text_layout("attached_assets/generated_images/chap8ban.jpg", layout="full")
    text111 = """
    <p> <div class='beth1'>You cannot control who stays or who leaves, but you can always control how brightly you rise again. - Danjin Master<br> <br>
    </p>

    """
    create_image_text_layout(text_content=text111, layout="full")
 