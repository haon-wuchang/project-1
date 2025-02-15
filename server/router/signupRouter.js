import express from "express";
import * as controller from '../controller/signupController.js';

const router = express.Router();

router.post('/dupliId',controller.getId);    // 아이디중복확인을 위한 서버



export default router;