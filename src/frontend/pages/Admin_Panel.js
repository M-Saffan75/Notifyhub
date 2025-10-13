import React from 'react'
import '../css/admin_styles.css';
import logo from '../img/logo.png';
import notice from '../img/notice.jpg';
import colors from '../../theme/Color';
import ButtonHere from '../../components/ButtonHere';
import SmallButton from '../../components/SmallButton';

const Admin_Panel = () => {
    return (
        <>

            <div id='container'>

                <div id='logo_area_container'>

                    <div id="logo_area" style={{ backgroundColor: colors.light_grey }}>
                        <img src={logo} className='logo_here' alt='logo here' />
                        <div className='logo_name' style={{ color: colors.secondary }}>gc university hyderabad</div>
                    </div>

                    <div className='down_notice_area' style={{ backgroundColor: colors.light_grey }}>

                        <div className='btn_area'>
                            <ButtonHere btn_text={'academic notices'} />
                        </div>

                        <div className='notice_here_outline' style={{ borderColor: colors.secondary }}>
                            <div>
                                <SmallButton />
                            </div>
                            <img src={notice} className='notice_here' alt='logo here' style={{ borderColor: colors.secondary }} />
                        </div>

                    </div>

                    {/* <div>
                        btn component
                    </div>
                    <div id='table_brder'>
                        <div id='sub_table_brder'>
                            <div>
                                btn
                            </div>
                            <div>
                                <img src='' className='' />
                            </div>
                        </div>
                    </div> */}
                </div>

                <div className='center_area'>

                </div>

                <div className='third_area'>

                </div>

            </div>

        </>
    )
}

export default Admin_Panel