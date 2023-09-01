import React from 'react';
import {
    Container,
    Image
  } from "./ServerError.styled";
  import img from "../../images/server-error.png";

const NotFound = () => {
  return (
    <Container>
    <Image src={img} alt="image"/>
    </Container>
  );
};

export default NotFound;