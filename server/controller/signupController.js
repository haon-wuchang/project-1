
export const getId = (req,res) => {
    const result = repository.getId(req.body);
    res.json(result);
    res.end();
}