import { db } from './db.js';

/** 관리자 페이지 로그인 - select **/
export const checkAdminLogin = async({id, pwd}) => { // 수정 필요 : 테이블명, 컬럼명
    const sql = `
        select count(*) as result_rows
        from admins
        where username = ? and password = ?
    `;

    const [result] = await db.execute(sql, [id, pwd]);

    return result[0];
}

/** 관리자 페이지 고객 정보 호출 **/
export const getCustomerData = async() => {
    const sql = `
        select customer_id,
                name,
                username,
                email,
                phone,
                address,
                left(birth_date, 10) as birth_date,
                membership_level
        from customers
    `;

    const [result] = await db.execute(sql);

    return result;
}

/** 관리자 페이지 상품 정보 호출**/
export const getProductData = async() => {
    console.log('1111');
    
    const sql = `
        select  pid,
                category,
                sub_category,
                name,
                color,
                size,
                likes,
                star,
                stock,
                original_price,
                discount_rate,
                discounted_price
        from products
    `;

    const [result] = await db.execute(sql);

    return result;
}