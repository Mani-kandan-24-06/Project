//import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router,Routes,Route } from 'react-router-dom';
import Login from './Component/Login';
import Admin from './Component/Admin';
import Quiz from './Component/Quiz';
import Welcome from './Component/Welcome';
import AdminLogin from './Component/AdminLogin';

function App() {
  return (
    <div className="Login">
     <Router>
      <Routes>
        <Route path="/" element={<Welcome />} />
        <Route path="/Admin" element={<Admin />} />
        <Route path="/Candidate" element={<Quiz/>} />
        <Route path="/CandidateLogin" element={<Login/>} />
        <Route path="/AdminLogin" element={<AdminLogin/>} />
       </Routes>
     </Router>
    </div>
  );
}

export default App;