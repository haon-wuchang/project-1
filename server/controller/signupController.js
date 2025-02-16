
export const getId = async (req,res) => {
    const result = await repository.getId(req.body);
    res.json(result);
    res.end();
}


export const registCustomer = async(req,res) => {
    const result = await repository.registCustomer(req.body);
    res.json(result);
    res.end();
}