import React, { useEffect, useState } from 'react';

const CaptchaCard = () => {
    const [captcha, setCaptcha] = useState(null);
    const [selection, setSelection] = useState('');
    const [result, setResult] = useState(null);

    useEffect(() => {
        const fetchCaptcha = async () => {
            const response = await fetch('http://localhost:8000/captcha/get-captcha/');
            const data = await response.json();
            setCaptcha(data);
        };

        fetchCaptcha();
    }, []);

    const handleSelectionChange = (event) => {
        setSelection(event.target.value);
    };

    const handleSubmit = async () => {
        const response = await fetch('http://localhost:8000/captcha/validate-captcha/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ selection, captcha_id: captcha.id }),
        });

        const data = await response.json();
        setResult(data.result);
    };

    return (
        <div>
            {captcha ? (
                <>
                    <p>{captcha.instruction}</p>
                    <select value={selection} onChange={handleSelectionChange}>
                        <option value="">Select an option</option>
                        {captcha.options.map((option) => (
                            <option key={option.id} value={captcha.captcha_type === 'text' ? option.text : option.image_url}>
                                {captcha.captcha_type === 'text' ? option.text : (
                                    <img src={option.image_url} alt="captcha option" width={50} height={50} />
                                )}
                            </option>
                        ))}
                    </select>
                    <button onClick={handleSubmit}>Submit</button>
                    {result && <p>{result === 'success' ? 'Captcha Passed!' : 'Captcha Failed'}</p>}
                </>
            ) : (
                <p>Loading captcha...</p>
            )}
        </div>
    );
};

export default CaptchaCard;
