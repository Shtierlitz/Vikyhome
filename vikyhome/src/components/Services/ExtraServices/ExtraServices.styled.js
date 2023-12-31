import styled from 'styled-components';
import DEVICE from "../../../constants/deviceSize";

export const WrapBtn = styled.div`
margin-bottom: 60px;
background-color: transparent;
color: transparent;
border: none;

`;

export const CloseButton = styled.button`
  width: 50px;
  height: 50px;
  border: none;
  cursor: pointer;
  font-family: inherit;
  position: absolute;
  top: 20px;
  right: 15px;
  background-color: ${p => p.theme.colors.colorPink};
  font-size: 30px;
  @media ${DEVICE.tablet} {
    right: 20px;
  }
  @media ${DEVICE.laptop} {

  }
`;

export const ModalDescription = styled.p`
  color: ${p => p.theme.colors.colorWhite};
  font-size: 15px;
  margin-right: 10px;
  user-select: none;

  @media ${DEVICE.tablet} {
  }
  @media ${DEVICE.laptop} {
    font-size: 30px;
    margin-right: 20px;
  }
`;

export const ModalPrice = styled.p`
  color: ${p => p.theme.colors.titleMainColor};
  font-size: 18px;
  margin-left:auto;
  user-select: none;

  @media ${DEVICE.tablet} {
  }
  @media ${DEVICE.laptop} {
    font-size: 30px;
    
  }
`;

export const ModalPriceDesc = styled.p`
  color: ${p => p.theme.colors.titleMainColor};
  font-size: 15px;
  margin-left: 5px;
  user-select: none;

  @media ${DEVICE.tablet} {

  }
  @media ${DEVICE.laptop} {
    font-size: 28px;
    margin-left: 10px;
  }
`;

export const Backdrop = styled.div`
  position: fixed;
  left: 0;
  top: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 15px;
  width: 100vw;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.4);
`;

export const ModalContainer = styled.div`
 max-width: 800px;
  max-height: 700px;
  position: relative;
  background-color: ${p => p.theme.colors.colorPink};
  overflow: auto; 
  padding: 10px; 
  text-align: start;
  border: 5px solid #8d8d8dac;
border-radius: 20px;

  @media ${DEVICE.tablet} {
    max-width: 1000px;
  max-height: 800px;
  }
  @media ${DEVICE.laptop} {

 padding: 20px; 
  }
`;

export const ModalText = styled.div`
  margin-bottom: 20px;
  display: flex;
align-items: center;
justify-content: center;
user-select: none;
`;