
import axios from "axios";
import {Navigate} from "react-router-dom";
import {useState} from "react";
import compu from '../imagenes/computadora.png';
import '../component/estilo.css';
export const Login = () => {
    const [nombreUsuario, setNombreUsuario] = useState('');
    const [contrasena, setContrasena] = useState('');

    const submit = async e => {
        e.preventDefault();

        const user = {
            username: nombreUsuario,
            password: contrasena
          };

        const {data} = await axios.post('http://localhost:8000/token/', user ,{headers: {
            'Content-Type': 'application/json'
        }}, {withCredentials: true});

        console.log(data)
        localStorage.clear();
        localStorage.setItem('access_token', data.access);
        localStorage.setItem('refresh_token', data.refresh);
        axios.defaults.headers.common['Authorization'] = `Bearer ${data['access']}`;
        window.location.href = '/'

    }

    return(
        <div className="Auth-form-container">
        <form className="Auth-form" onSubmit={submit}>
        <div class="icono">
          <img src={compu}/>
        </div>
          
          <div className="Auth-form-content">
            <h3 className="Auth-form-title">CompuSpace</h3>
            <div className="form-group mt-3">
            
              <input
                className="form-control mt-1"
                placeholder="Usuario"
                name='username'
                type='text'
                value={nombreUsuario}
                required
                onChange={e => setNombreUsuario(e.target.value)}
              />
            </div>
            <div className="form-group mt-3">
              
              <input
                name='password'
                type="password"
                className="form-control mt-1"
                placeholder="Contraseña"
                value={contrasena}
                required
                onChange={e => setContrasena(e.target.value)}
              />
            </div>
            <div className="boton">
              <button type="submit" className="btn btn-primary">
                INICIAR SESION
              </button>
            </div>
          </div>
        </form>
    </div>

    )
}
