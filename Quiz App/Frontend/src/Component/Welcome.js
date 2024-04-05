import { Link } from "react-router-dom";

function Welcome () {
 return (
    <div>
       <Link to ="/AdminLogin"> AdminLogin</Link> 
       <Link to ="/CandidateLogin"> CandidateLogin</Link> 
    </div>
 )
}
export default Welcome;