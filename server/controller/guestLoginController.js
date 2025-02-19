import * as repository from '../repository/guestLoginRepository.js';
import jwt from 'jsonwebtoken';

export const checkGuestLogin = async (req, res) => {
    let result = await repository.checkGuestLogin(req.body);

    if (result.result_rows === 1) {
        console.log(result.result_rows);
        const rawToken = jwt.sign({ "username": req.body.name }, '7mPjPeZ7Ul');
        const guestToken = `guest_token_${rawToken}`; //  guest_token_ 추가
        result = { ...result, "token": guestToken };  
    }

    res.json(result);
    res.end();
};
