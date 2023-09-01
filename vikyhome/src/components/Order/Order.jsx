import {
    Container,
    Title,
    ContactItem,
    ContactBox,
   
  } from "../Order/Order.styled";

  
  
  const Order = () => {
    return (
      <Container >
        <Title> Замовити послуги: </Title>
  
        <ContactBox>
          <ContactItem>
         
            <a
              href="tel:+380685073544"
              style={{ textDecoration: "none", color: "#000",  display: "flex",
              alignItems: "center", marginBottom: "10px",  }}
            >
            
              Зателефонувати  (068)507-3544
            </a>
          </ContactItem>
          <ContactItem>
         
            <a
              href="mailto:vikyhome.kyiv@gmail.com"
              style={{ textDecoration: "none", color: "#000",  display: "flex",
              alignItems: "center", }}
            >
             
             Замовити через е-mail
            </a> 
            </ContactItem>
            <ContactItem>
                    <a
          href="https://www.instagram.com/vikyhome_kyiv/"
          target="_blank"
          rel="noopener noreferrer"
          style={{ textDecoration: "none", color: "#000",  display: "flex",
              alignItems: "center", marginBottom: "10px",  }}
        >
           Замовити в  Instagram
         
        </a>
            </ContactItem>
        <ContactItem>
            <a
          href="https://t.me/vikiyhome"
          target="_blank"
          rel="noopener noreferrer"
          style={{ textDecoration: "none", color: "#000",  display: "flex",
              alignItems: "center", marginBottom: "10px",  }}
        >
            Замовити в Telegram
         
        </a>   
        </ContactItem>
     
         
        </ContactBox>
  
     
      </Container>
    );
  };
  
  export default Order;