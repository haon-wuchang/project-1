import * as repository from '../repository/signupRepository.js';

//아이디 가져와서 중복체크
export const getId = async (req,res) => {
    const result = await repository.getId(req.body);
    res.json(result);
    res.end();
}

// 회원 등록
export const registCustomer = async(req,res) => {
    // console.log('회원가입',req.body);
    
    const result = await repository.registCustomer(req.body);
    res.json(result);
    res.end();
}