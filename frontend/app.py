import streamlit as st
import requests

st.set_page_config(layout="wide")

st.markdown("""
<style>
body {background: #0e1117; color: white;}
.card {background:#0e1117;padding:20px;border-radius:12px;margin:10px;color: white !important;}
.card * {color: white !important;}
</style>
""", unsafe_allow_html=True)

st.title("🤖 Grid07 AI (Production)")

post = st.text_area("Enter your post")

if st.button("Run"):
    try:
        res = requests.post(
            "http://localhost:8000/generate",
            json={"post": post}
        )

        # 🔍 Debug info (VERY IMPORTANT)
        st.write("Status Code:", res.status_code)

        # ❌ If backend error
        if res.status_code != 200:
            st.error(f"Backend Error: {res.text}")
        else:
            try:
                data = res.json()  # ✅ safe parse

                st.subheader("Matched Bots")
                st.write(data.get("bots", []))

                st.subheader("Responses")
                for r in data.get("responses", []):
                    st.markdown(f"<div class='card'>{r}</div>", unsafe_allow_html=True)

            except Exception:
                st.error("Invalid JSON received from backend")
                st.text(res.text)  # show raw response

    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to backend. Make sure FastAPI is running on port 8000")

    except Exception as e:
        st.error(f"Unexpected Error: {e}")


# if st.button("Run"):
#     res = requests.post(
#     "http://localhost:8000/generate",
#     json={"post": post}
#     )
#     data = res.json()
#
#     st.subheader("Matched Bots")
#     st.write(data["bots"])
#
#     st.subheader("Responses")
#     for r in data["responses"]:
#         st.markdown(f"<div class='card'>{r}</div>", unsafe_allow_html=True)


# import streamlit as st
# from personas import personas
# from router import route_post
# from graph import build_graph
#
# st.set_page_config(page_title="Grid07 AI", layout="wide")
#
# st.markdown("""
# <style>
# body {background-color:#0e1117; color:white;}
# .big {font-size:30px; font-weight:bold;}
# </style>
# """, unsafe_allow_html=True)
#
# st.markdown('<p class="big">🤖 Grid07 AI System</p>', unsafe_allow_html=True)
#
# user_input = st.text_area("Enter Post")
#
# if st.button("Run AI"):
#     bots = route_post(user_input)
#     st.write("### Matched Bots", bots)
#
#     graph = build_graph()
#
#     for b in bots:
#         res = graph.invoke({"persona": personas[b], "bot_id": b})
#         st.json(res)