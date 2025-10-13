import React from 'react'
import colors from '../theme/Color'
import images from '../images/Image'

const SmallButton = ({
    btn_text, Color, backgroundColor, fontSize, src,
    textTransform, borderRadius, border, height, width
}) => {

    return (
        <>
            <div>
                <button className='btn_here'
                    style={{
                        width: '40%',
                        padding: '1.2% 2%',
                        cursor: 'pointer',
                        fontWeight: 'bold',
                        fontSize: fontSize ?? 8,
                        color: Color ?? colors.primary,
                        borderRadius: borderRadius ?? 5,
                        textTransform: textTransform ?? 'capitalize',
                        backgroundColor: backgroundColor ?? colors.success,
                        border: border ? border : `2px solid ${colors.success}`,

                        display: 'flex',
                        flexDirection: 'row',
                        alignItems: 'center',
                        justifyContent: 'space-between'
                    }}>
                    update
                    <div style={{

                        display: 'flex',
                        alignItems: 'center',
                        flexDirection: 'row',
                        justifyContent: 'center',
                    }}>
                        <img src={src ?? images.editicon} alt='icon'
                            height={height ?? 10}
                            width={width ?? 10}
                            style={{ backgroundSize: 'cover', objectFit: 'contain' }}
                        />
                    </div>
                </button>
            </div>
        </>
    )
}

export default SmallButton