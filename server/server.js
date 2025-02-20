import express from 'express';
import cors from 'cors';
import signupRouter from './router/signupRouter.js';
import mysql from 'mysql2/promise'; // MySQL 연동을 위한 패키지
import loginRouter from './router/loginRouter.js'
import productRouter from './router/productRouter.js';

const server = express();
const port = 9000;

/* 서버의 공통적인 작업 */
server.use(express.json());
server.use(express.urlencoded()); 
server.use(cors());

// 서버의 요청처리를 위한 미들웨어 정의 //
server.use('/user', signupRouter);
// server.use('/user', loginRouter);
server.use('/product', productRouter);




server.listen(port,()=>{
    console.log('서버실행중');
    
});