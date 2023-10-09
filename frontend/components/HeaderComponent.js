
import React from 'react';

const HeaderComponent = () => {
    return (
        <header>
            <div className='logo'>
                <img src='/static/logo.png' alt='Logo' />
            </div>
            <nav>
                <ul>
                    <li><a href='#'>Inicio</a></li>
                    <li><a href='#'>Sobre</a></li>
                    <li><a href='#'>Servicios</a></li>
                    <li><a href='#'>Contactar</a></li>
                </ul>
            </nav>
        </header>
    );
};

export default HeaderComponent;