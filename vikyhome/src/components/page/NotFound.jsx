import React from 'react';
import {
    Container,
    Image
  } from "./NotFound.styled";
  import img from "../../images/not-found.jpg";
 

const NotFound = () => {
  return (
    <Container>
    <Image src={img} alt="image"/>
    </Container>
  );
};

export default NotFound;