import styled from 'styled-components';
import DEVICE from "./../../constants/deviceSize";



export const Container =styled.div`
background-color:  ${p => p.theme.colors.colorPink};
box-shadow: 10px 10px 10px rgba(173, 18, 18, 0.12),
10px 10px 10px rgba(86, 83, 83, 0.969),
10px 10px 10px rgba(169, 162, 162, 0.2);
border-radius: 20px 20px 20px 20px;
font-weight:700;
padding: 20px;
margin-right:auto;
margin-left:auto;
margin-bottom: 20px;

@media ${DEVICE.tablet} {

}
@media ${DEVICE.laptop} {

}
`;

export const Title = styled.h1`
 /* font-family: cursive; */
 color: ${p => p.theme.colors.titleMainColor};
  font-size: 45px;
  margin-bottom: 20px;

@media ${DEVICE.tablet} {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 40px;
  margin-bottom: 20px;
}
@media ${DEVICE.laptop} {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 65px;
  margin-bottom: 20px;
 
 
}
`;

export const ContactItem =styled.li`
color: ${p => p.theme.colors.titleMainColor};
text-decoration: none;
display: flex;
justify-content: center;
align-items: center;
border: 5px solid #9f0e6f;
border-radius: 20px;
&:hover {
    box-shadow: 10px  20px 20px rgb(159, 14, 111);
 }
 width: 300px;
height: 90px;
font-size: 24px;
margin-bottom: 20px;
margin-right: 10px;

 @media ${DEVICE.tablet} {
    flex-basis: calc(50% - 25px);
  font-size: 28px;
  margin-right: 25px;
}
@media ${DEVICE.laptop} {
    width: 400px;
    height: 90px;
    font-weight:700;
  font-size: 34px;
  margin-right: 25px;
 }

`;

export const ContactBox =styled.div`
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    cursor: pointer;
    margin-top: 15px;
   

@media ${DEVICE.tablet} {
    
}
@media ${DEVICE.laptop} {
    display: flex;
    justify-content: center;
    margin-bottom: 50px;
    margin-top: 30px;
}

`;

