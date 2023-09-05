import styled from 'styled-components';
import DEVICE from "../../constants/deviceSize";


export const Wrapper =styled.div`
padding: 20px;
margin-right:auto;
margin-left:auto;
margin-bottom: 20px;
background-color: #8d8d8dac;
box-shadow: 10px 10px 10px rgba(173, 18, 18, 0.12),
10px 10px 10px rgba(86, 83, 83, 0.969),
10px 10px 10px rgba(169, 162, 162, 0.2);
border-radius: 20px;
user-select: none;

@media ${DEVICE.mobile} {
display: block;
}
@media ${DEVICE.tablet} {
  display:flex;
justify-content: space-around;
}
@media ${DEVICE.laptop} {
  display:flex;
justify-content: space-around;
}
`;

export const Title = styled.h1`
 color: ${p => p.theme.colors.titleMainColor};
 text-align: center;
  font-size: 25px;
  user-select: none;
  margin-bottom: 20px;

@media ${DEVICE.tablet} {
  font-size: 35px;
}
@media ${DEVICE.laptop} {
  font-size: 40px;
 
}
`;

export const PostLi =styled.ul`
margin-bottom: 20px;


@media ${DEVICE.tablet} {
  margin-bottom: 10px;
  margin-top: 10px;
}
@media ${DEVICE.laptop} {
  margin-bottom: 10px;
  margin-top: 20px;
}
`;

export const Text =styled.ul `
font-size: 20px;
color: ${p => p.theme.colors.titleMainColor};
user-select: none;

@media ${DEVICE.tablet} {
    font-size: 25px;
  
}
@media ${DEVICE.laptop} {
  font-size: 30px;
}
`;

export const List =styled.li`


`;

export const Box =styled.div`

text-align: left;
border: 7px solid ${p => p.theme.colors.colorPink};
border-radius: 20px;
margin-bottom: 20px;
padding: 15px;
user-select: none;

@media ${DEVICE.tablet} {
  padding: 20px;
}
@media ${DEVICE.laptop} {
  padding: 35px;
}
`;

export const PostBtn = styled.button`
cursor: pointer;
  font-size: 25px;
  display: flex;
  justify-content: center;
align-items: center;
  background-color:  ${p => p.theme.colors.colorPink};
  margin-bottom: 40px;
  margin-top: 40px;
  width: 230px;
height: 75px;
border-radius: 20px;
  border: none;
  user-select: none;

  transition: background-color 0.4s;
 &:hover {
  box-shadow: 10px  20px 20px rgb(159, 14, 111);
 }

  @media ${DEVICE.tablet} {
    font-size: 30px;
    width: 400px;
}
@media ${DEVICE.laptop} {
  width: 400px;
  font-size: 40px;
}
`;

export const PostContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`;
