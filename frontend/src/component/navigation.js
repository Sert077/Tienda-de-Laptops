import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import React, { useState, useEffect} from 'react';

export function Navigation() {
  const [isAuth, setIsAuth] = useState(false);

  useEffect(() => {
    if (localStorage.getItem('access_token') !== null) {
      setIsAuth(true);
    }
  }, [isAuth]);

  return (
    
    <div>
        <Navbar style={{ backgroundColor: "#243757 " }}>
          <Navbar.Brand href="/" style={{ color: "white" }}>CompuSpace</Navbar.Brand>
          <Nav className="mr-auto">
            {isAuth ? (
              <>
                <Nav.Link href="/" style={{ color: "white" }}>Home</Nav.Link>
                <Nav.Link href="/laptops" style={{ color: "white" }}>Laptops</Nav.Link>
              </>
            ) : null}
          </Nav>
          <Nav className="ml-auto">
            {isAuth ? (
              <Nav.Link href="/logout" style={{ color: "white" }}>Logout</Nav.Link>
            ) : (
              <Nav.Link href="/login" style={{ color: "white" }}>Login</Nav.Link>
            )}
          </Nav>
        </Navbar>
      </div>
  );
}
