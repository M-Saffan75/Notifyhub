import React from 'react';
import logo from '../img/logo.png';
import '../css/pages_styles.css'

const Admin_Login = () => {
    return (
        <>
            <div className="main-container">

                {/* Top Bar */}

                <header className="topbar">
                    <div className="logo-title">
                        <img src={logo} alt="Logo" className="logo" />
                        <h1 className="title">GC UNIVERSITY HYDERABAD</h1>
                    </div>
                </header>

                {/* Center Login Box */}

                <div className="center-box">
                    <div className="login-card">

                        <div>
                            <h2 className="login-heading">Login to Dashboard</h2>
                            <div className='underline'></div>
                        </div>

                        <div className='inpt_area' id='inpt_area1'>
                            <label className="label label_1">Your Email</label>
                            <input className="input_text" placeholder="Enter email" />
                        </div>

                        <div className='inpt_area'>
                            <label className="label_1">Your Password</label>
                            <input className="input_text" placeholder="Enter password" />
                        </div>

                        <div className="login-btn_area">
                            <button className="login-btn">Login</button>
                        </div>

                    </div>
                </div>

                {/* Footer */}
                <footer className="footer">
                    GC University Hyderabad, Kali Mori Hyderabad Sindh, Pakistan • Phone:
                    022-211995
                </footer>
            </div>
        </>
    )
}

export default Admin_Login