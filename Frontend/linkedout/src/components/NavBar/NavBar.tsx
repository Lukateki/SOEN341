import React from "react";
import { useNavigate } from "react-router-dom";
import { Box, Button, CardMedia, TextField } from '@mui/material';
import { isUserLoggedIn } from "../../main/pages/LoginPage/types";
import "./NavBar.css"

export const NavBar : React.FC  = () => {

    const navigate = useNavigate()

    const handleLoginClick = () => {
        navigate('/login');
      };
      const handleRegisterClick = () => {
        navigate('/register');
      }

    return(
      <body>
        <div className="navbar-header">
          <div className="navbar-left-header">
            <span className="navbar-company-name">Linked</span>
              <a id="logo" href="http://localhost:3000/">
                <img src="img/LinkedoutLogo2.png" alt="LinkedOut" className="home-logo" />
              </a>
              <div className="navbar-search-bar">
                <TextField size="small" id="outlined-basic" label="Search" placeholder="Search job postings"/>
              </div>
            </div>
            <div className="navbar-right-header">
              {isUserLoggedIn() ? 
              <Box>
                <a id="profile" href="http://localhost:3000/profile">
                <CardMedia 
                  component="img"
                  height="40px"
                  image='https://picsum.photos/200/200'
                  alt='profile picture'
                  className="navbar-picture"
                />
                </a>
              </Box>  
               :
              <div className="navbar-buttons">
                <Button onClick={handleLoginClick}>Login</Button>
                <Button onClick={handleRegisterClick}>Register</Button>
              </div>
              }
          </div>
        </div>
        </body>
    )
}

export default NavBar;