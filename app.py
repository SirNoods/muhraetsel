import random
import streamlit as st
st.header("Willkommen bei Jackys Muhrätselgenerator")
st.write("Die drei Buchstaben aus denen dein Rätsel generiert wird sind M, U und H.")
st.write("------------------------------------------")
riddletext =""
choices = ["M","U","H"]
rows = st.text_input("Wie viele Zeilen soll dein Rätsel haben?", "10")
st.write(str(rows)+" Zeilen.")
columns = st.text_input("Wie viele Zeichen sollen pro spalte in dem Rätsel sein?", "10")
st.write(str(columns)+" Zeichen pro Zeile.")
rows = int(rows)
columns = int(columns)

for x in range(0,rows):
    for i in range(0,columns):
        rlength = len(riddletext)
        # determining horizontal buffer
        horbuffer = riddletext[rlength - 2:]
        #print("HORIZONTAL: "+ horbuffer)
        # determining vertical buffer
        vertbuffer = ""
        if rlength > 46:
            temp = riddletext[rlength -((columns*2)+1):]
            vertbuffer += temp[0]
            temp = riddletext[rlength -(columns+1):]
            vertbuffer += temp[0]
            #print("VERTICAL: "+ vertbuffer)
        nextletter = random.choice(choices)
        if (horbuffer == "MU" and nextletter == "H") or (vertbuffer == "MU" and nextletter == "H"):
            #print("MUH DETECTED. INVALID!")
            #print("HORBUFFER: "+horbuffer + " VERTBUFFER: " + vertbuffer)
            #print("NEXT LETTER WOULD BE H")
            nextletter = random.choice(["M","U"])
            riddletext += nextletter
        else:
            riddletext += nextletter
    riddletext += "\n"

if "MUH" not in riddletext:
    print("MUH test bestanden.")

st.write(riddletext)