import streamlit as st

st.title("CineScore+ Ver 2")

option = st.sidebar.selectbox(
    "Choose an action:",
    ["Search", "Review", "Filter by Genre", "View Movieboard"]
)

if option == "Search":
    st.header("Search for a Movie")
    title = st.text_input("Enter a movie title")
    year = st.text_input("Enter a release year (optional)")
    if st.button("Search"):
        st.write("Search results displayed here.")

elif option == "Review":
    st.header("Review a movie.")

    # Search for a movie
    title = st.text_input("Search for a movie")
    year = st.text_input("Release Year (optional)")

    if st.button("Search"):
        results = search_movie(title, year)
        st.session_state["search_results"] = results
    

elif option == "Filter by Genre":
    st.header("Filter by Genre")
    st.write("Genre filter interfaec WIP.")

elif option == "View Movieboard":
    st.header("Movieboard")
    st.write("Movieboard display in progress.")


