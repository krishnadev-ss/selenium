import React,{ useState} from 'react'
import { useNavigate } from 'react-router-dom'

const Login = () => {

  const navigate = useNavigate()  

  // state for email and password
  const [email, setEmail] = useState('') 
  const [password, setPassword] = useState('')

  const handleChange = (e) => {
    const { name, value } = e.target
    name === 'email' ? setEmail(value) : setPassword(value)
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    if(email === 'hades@gmail.com' && password === 'hades123')
      navigate('/User')
    else
      navigate('/notfound')
  }

  return (
    <div>
      <form id="login-form" onSubmit={handleSubmit}>
        <label for="email">Email:</label>
        <input id="t-email" type="text" name="email" value={email} required onChange={handleChange}/> <br/><br/>
        <label for="password">Password:</label>
        <input id="t-password" type="password" name="password" value={password} required onChange={handleChange}/> <br/><br/>
        <button >Login</button>
      </form>
    </div>
  )
}

export default Login