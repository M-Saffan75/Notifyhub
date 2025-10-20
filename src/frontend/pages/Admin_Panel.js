import React from 'react';
import '../css/admin_styles.css';
import logo from '../img/logo.png';
import notice from '../img/notice.jpg';
import colors from '../../theme/Color';
import images from '../../images/Image';
import HeadBtn from '../../components/HeadBtn';
import ButtonHere from '../../components/ButtonHere';
import SmallButton from '../../components/SmallButton';
import HeadingHere from '../../components/HeadingHere';

const Admin_Panel = () => {

    const items = [1, 2];
    const itemtables = [1, 2, 3, 4]
    const ai_items = [1, 2]
    return (
        <>

            <div id='container'>

                <div id='logo_area_container'>

                    <div id="logo_area" style={{ backgroundColor: colors.light_grey }}>
                        <img src={images.logo} className='logo_here' alt='logo here' />
                        <div className='logo_name' style={{ color: colors.secondary }}>gc university hyderabad</div>
                    </div>

                    <div className='down_notice_area' style={{ backgroundColor: colors.light_grey }}>

                        <div className='btn_area'>
                            <ButtonHere btn_text={'academic notices'} />
                        </div>

                        {items.map((_, index) => (
                            <div
                                key={index}
                                className='notice_here_outline'
                                style={{ borderColor: colors.success }}>
                                <div style={{ display: 'flex', justifyContent: 'flex-end', marginBottom: '2%' }}>
                                    <SmallButton btn_text={'update'} />
                                </div>
                                <div>
                                    <img
                                        src={images.notice}
                                        className='notice_here'
                                        alt='update here'
                                        style={{ borderColor: colors.success }}
                                    />
                                </div>
                            </div>
                        ))}

                    </div>

                </div>

                {/*  */}

                <div className='center_area'>
                    <div className='headeing_qoute_area' style={{ backgroundColor: colors.light_grey }}>

                        <div className='row_head_area'>
                            <HeadingHere text={'Daily Quotes :'} fontSize={17} />
                            <SmallButton btn_text='update' fontSize={9} width={55} justifyContent={'center'} backgroundColor={colors.secondary} showbtnimg={false} />

                        </div>

                        <input className='inpt_hightlight' type='text' style={{ color: colors.secondary, outline: 'none' }} color={colors.secondary}
                            defaultValue={'"Education is the movement from darkness to light"'} maxLength={60} />
                    </div>

                    {/*  */}

                    <div className='image_area_here'
                        style={{
                            backgroundImage: `url(${images.alert_bg})`,
                        }}>
                        <div className='row_head_area'>

                            <HeadingHere text={'important alerts '} fontSize={16} ShowLine={true} width={'50%'}  /> 
                            <SmallButton btn_text='update' fontSize={9} width={55} justifyContent={'center'} backgroundColor={colors.secondary} showbtnimg={false} />
                        
                        </div>

                        <textarea className='inpt_alert_text' type='text' maxLength={180}
                            style={{ backgroundColor: 'transparent', resize: 'none', color: colors.secondary, outline: 'none', border: `1px solid ${colors.secondary}`, }} defaultValue=
                            {"Hey everyone! Our Academic Notices section has been refreshed with new updates and important announcements.Make sure to check it out so you don’t miss anything important."} />

                    </div>

                    {/*  */}

                    {/*  */}

                    <div className='timetable_area' style={{ backgroundColor: colors.light_grey }}>

                        <div style={{ display: 'flex', alignItems: 'center' }}>
                            <HeadBtn text={'department timetables '} width={'50%'} fontSize={16} />
                        </div>

                        {/*  */}

                        <div className='timetable_row_area'
                        // style={{ backgroundColor: 'green' }}
                        >
                            {itemtables.map((_, index) => (
                                <div
                                    key={index}
                                    className='timetable_here_outline'
                                    style={{ borderColor: colors.secondary }}>
                                    <div style={{ display: 'flex', justifyContent: 'flex-end', marginBottom: '2%' }}>
                                        <SmallButton btn_text={'update'} backgroundColor={colors.secondary} />
                                    </div>
                                    <div>
                                        <img
                                            src={images.time_table}
                                            className='timetable_img_here'
                                            alt='update here'
                                            style={{ borderColor: colors.secondary }}
                                        />
                                    </div>
                                </div>
                            ))}
                        </div>

                        {/*  */}

                    </div>

                    {/*  */}

                </div>


                <div className='third_area'>

                    {/*  */}

                    <div className='main_btn_area' style={{ backgroundColor: colors.light_grey }}>

                        <div className='btn_area_mid_term'>

                            <div className='row_head_area'>
                                <HeadingHere text={'Exams updates'} ShowLine={true} fontSize={12} width={'50%'} />
                                <SmallButton btn_text='update' fontSize={9} width={50} justifyContent={'center'} backgroundColor={colors.success} showbtnimg={false} />
                            </div>

                            <input type='text' defaultValue={'mid term : september-october'} maxLength={34} className='mid_term_inpt'
                                style={{ outline: 'none', border: `1px solid ${colors.success}`, }}
                            />
                        </div>

                    </div>

                    {/*  */}

                    <div className='sub_third_area' style={{ backgroundColor: colors.light_grey, }}>

                        <div className='row_head_area' >
                            <HeadingHere text={'students achievements'} ShowLine={true} fontSize={12} width={'50%'} />
                            <SmallButton btn_text='update' fontSize={9} width={50} justifyContent={'center'} backgroundColor={colors.success} showbtnimg={false} />
                        </div>

                        {/*  */}

                        <div className='point_hightlight_area'>
                            <textarea className='point_hightlight' type='text' style={{ color: colors.black, outline: 'none', border: `1px solid ${colors.success}`, resize: 'none', backgroundColor: 'transparent', }}
                                defaultValue={"CS students won 1st place in National Coding Hackathon 2025."} maxLength={100} />
                            <textarea className='point_hightlight' type='text' style={{ color: colors.black, outline: 'none', border: `1px solid ${colors.success}`, resize: 'none', backgroundColor: 'transparent', }}
                                defaultValue={"Business team earned PKR 500k HEC Startup Pakistan grant."} maxLength={100} />
                            <textarea className='point_hightlight' type='text' style={{ color: colors.black, outline: 'none', border: `1px solid ${colors.success}`, resize: 'none', backgroundColor: 'transparent', }}
                                defaultValue={"Computer Science students selected for Erasmus Exchange Program in Turkey."} maxLength={100} />
                            <textarea className='point_hightlight' type='text' style={{ color: colors.black, outline: 'none', border: `1px solid ${colors.success}`, resize: 'none', backgroundColor: 'transparent', }}
                                defaultValue={"GCUH Cricket Team won Inter-Collegiate Championship Trophy 2025."} maxLength={100} />
                        </div>

                        {/*  */}

                    </div>

                    {/*  */}

                    <div className='ai_keyword_area' style={{ backgroundColor: colors.light_grey }}>

                        {/*  */}
                        <div style={{ margin: "0 2%", width: '50%' }} >
                            <HeadingHere text={'students AI fAQs'} ShowLine={true} fontSize={12} width={'35%'} />
                        </div>
                        <div className='bg_keyword_area'>

                            {ai_items.map((_, index) => (
                                <div key={index} className='sub_ai_keywords_area' style={{ backgroundColor: colors.deep_grey }}>
                                    <div style={{ display: 'flex', flexDirection: 'row', padding: "0 3% 0 3%" ,justifyContent:'space-between'}}>
                                        <input className='ai_keywords_input' type='text' defaultValue={'sir zeeshan ki class kab hai ?'}
                                            style={{ border: `1px solid ${colors.success}`, backgroundColor: 'transparent', }} maxLength={30} />
                                        <SmallButton btn_text='update' showbtnimg={false} width={40} />
                                    </div>
                                    <div>
                                        <textarea className='ai_keywords_input_answer' type='text'
                                            defaultValue={'sir zeeshan ki class subha 10:20 se 11:10 tak hoti hai cs department mein part || students.'} rows={3}
                                            style={{ border: `1px solid ${colors.success}`, resize: 'none', backgroundColor: 'transparent', color: colors.grey, margin: "2% 3% 0 3%", outline: 'none', }}  maxLength={150} />
                                    </div>
                                </div>
                            ))}

                        </div>

                        {/*  */}

                    </div>

                    {/*  */}

                </div>

                {/*  */}

            </div>
            <div style={{ backgroundColor: colors.secondary, width: '100%', height: 31 }}></div>

        </>
    )
}

export default Admin_Panel