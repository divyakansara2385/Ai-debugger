import streamlit as st

from analyzer.repository import clone_repository, get_source_files
from analyzer.analyzer import analyze_file


st.set_page_config(
    page_title="AI Code Debugging Assistant",
    page_icon="🐛",
    layout="wide"
)


st.title("🐛 AI Code Debugging Assistant")

st.write(
    "Analyze Python code from a GitHub repository "
    "and receive NLP-based explanations and suggested fixes."
)


repo_url = st.text_input(
    "Enter GitHub Repository URL"
)


if st.button("Analyze Repository"):

    if not repo_url:
        st.warning("Please enter a GitHub repository URL.")

    else:

        with st.spinner("Cloning and analyzing repository..."):

            try:

                repo_path = clone_repository(repo_url)

                files = get_source_files(repo_path)

                python_files = [
                    file for file in files
                    if file["language"] == "Python"
                ]

            except Exception as e:

                st.error(f"Unable to analyze repository: {e}")
                st.stop()


        st.success(
            f"Found {len(python_files)} Python file(s)."
        )


        if not python_files:

            st.info(
                "No Python files were found in this repository."
            )

        else:

            for file in python_files:

                st.subheader(file["path"])

                result = analyze_file(file["path"])

                if not result["errors"]:

                    st.success("No errors detected.")

                    continue


                for error in result["errors"]:

                    st.error(
                        f"{error['type']} — Line {error['line']}"
                    )


                    if "variable" in error:

                        st.write(
                            f"**Variable:** `{error['variable']}`"
                        )


                    if "explanation" in error:

                        st.write(
                            "**Explanation:**"
                        )

                        st.write(
                            error["explanation"]
                        )


                    if "suggested_fix" in error:

                        st.write(
                            "**Suggested Fix:**"
                        )

                        st.write(
                            error["suggested_fix"]
                        )


                    if "similarity" in error:

                        st.write(
                            f"**NLP Similarity:** "
                            f"{error['similarity']:.2f}"
                        )

                    st.divider()