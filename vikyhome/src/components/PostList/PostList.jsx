import axios from "axios";
import React, { useEffect, useState, useCallback } from "react";
import {
  Wrapper,
  Title,
  Text,
  List,
  PostLi,
  Box,
  PostBtn,
  PostContainer,
} from "./PostList.styled";

const PostList = () => {
  const [posts, setPosts] = useState([]);
  const [isListOpen, setIsListOpen] = useState(false);

  const apiUrl = process.env.REACT_APP_URL_SECRET;

  const fetchPosts = useCallback(async () => {
    try {
      const response = await axios.get(`${apiUrl}/api/v1/post/`);
      setPosts(response.data);
    } catch (error) {
      console.error("Помилка при отриманні постів:", error);
    }
  }, [apiUrl]);
  
  useEffect(() => {
    fetchPosts();
  }, [fetchPosts]);

  


  return (
    <Wrapper>
    <PostContainer>
      <PostBtn onClick={() => setIsListOpen(!isListOpen)}>
        {isListOpen ? "Згорнути" : "Блог"}
      </PostBtn>
      <PostLi>
        {isListOpen && (
          <List>
            {posts.map((post) => (
              <Box key={post.id}>
                
                  <Title>{post.title}</Title>
                  <Text>
                    {post.text.split("\n").map((line, index) => (
                      <React.Fragment key={index}>
                        {line}
                        <br />
                      </React.Fragment>
                    ))}
                  </Text>
                
              </Box>
            ))}
          </List>
        )}
      </PostLi>
    </PostContainer>
  </Wrapper>
  );
};

export default PostList;



