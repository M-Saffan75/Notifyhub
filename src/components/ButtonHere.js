import React from 'react';
import colors from '../theme/Color';
import images from '../images/Image';

const ButtonHere = ({
    btn_text, Color, backgroundColor, fontSize, src,
    textTransform, borderRadius, border, height, width
}) => {

    return (

        <div>
            <button className='btn_here'
                style={{
                    width: '100%',
                    padding: '2% 2%',
                    cursor: 'pointer',
                    fontWeight: 'bold',
                    fontSize: fontSize ?? 8,
                    color: Color ?? colors.primary,
                    borderRadius: borderRadius ?? 100,
                    textTransform: textTransform ?? 'uppercase',
                    backgroundColor: backgroundColor ?? colors.secondary,
                    border: border ? border : `2px solid ${colors.secondary}`,

                    display: 'flex',
                    flexDirection: 'row',
                    alignItems: 'center',
                    justifyContent: 'space-between'
                }}
            >

                <div style={{
                    backgroundColor: colors.primary,
                    height: 20, width: 20, borderRadius: 100,

                    display: 'flex',
                    alignItems: 'center',
                    flexDirection: 'column',
                    justifyContent: 'center',
                }}>
                    <img src={src ?? images.downarrow} alt='icon'
                        height={height ?? 10}
                        width={width ?? 10}
                        style={{ backgroundSize: 'cover', objectFit: 'contain' }}
                    />
                </div>

                <div style={{ position: 'relative', right: '22%', }}>
                    {btn_text}
                </div>

            </button>

        </div>

    )
}

export default ButtonHere