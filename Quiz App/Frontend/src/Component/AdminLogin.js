import axios from "axios";
import {Navigate, useNavigate, useNavigation} from "react-router-dom";
import {useState} from "react";

export const AdminLogin = () => {
    const url = "http://localhost:8080/api/v1/auth/authenticate";

    const [token, setToken]= useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const Nav=useNavigate();


    const submit = async e => {
        e.preventDefault();

        const {data} = await axios.post(url, {
            email, password
        }, {withCredentials: false});
        Nav("/Admin",{state:{data:data.access_token}})
        axios.defaults.headers.common['Authorization'] = `Bearer ${data['access_token']}`;
        
    }




    return <main className="form-signin">
        <form onSubmit={submit}>
            <h1 className="h3 mb-3 fw-normal">Please sign in</h1>

            

            <div className="form-floating">
                <input type="email" className="form-control" id="floatingInput" placeholder="name@example.com"
                       onChange={e => setEmail(e.target.value)}
                />
                <label htmlFor="floatingInput">Email address</label>
            </div>

            <div className="form-floating">
                <input type="password" className="form-control" id="floatingPassword" placeholder="Password"
                       onChange={e => setPassword(e.target.value)}
                />
                <label htmlFor="floatingPassword">Password</label>
            </div>

            <button className="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
        </form>
    </main>
}
export default AdminLogin;
