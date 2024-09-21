from services import graph
import json
import streamlit as st

def main():
    st.title("Shortest Path Finder")

    # User input for vertices
    N = st.number_input("Number of Vertices", min_value=1, value=3)
    
    # User input for edges
    edges_input = st.text_area("Enter edges as JSON (e.g., [[0,1,100],[1,2,100],[0,2,500]])", 
                                value='[[0,1,100],[1,2,100],[0,2,500]]')
    
    # User input for start and end
    START = st.number_input("Start Vertex", min_value=0, value=0)
    END = st.number_input("End Vertex", min_value=0, value=2)
    MAX_STOPS = st.number_input("Max Stops", min_value=0, value=1)

    if st.button("Find Shortest Path"):
        try:
            edges = json.loads(edges_input)
            g = graph(N)

            for edge in edges:
                g.add_edge(edge[0], edge[1], edge[2])

            distance, path = g.bellman(START, END, MAX_STOPS)
            
            # Display the results
            st.success(f"Distance: {distance}")
            st.success(f"Path: {' -> '.join(map(str, path))}")
        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()