export default {
    name: 'action',
    type: 'document',
    title: 'Action',
    fields: [
        {
            name: 'action',
            type: 'string',
            title: 'Action',
        },
        {
            name: 'actionType',
            type: 'reference',
            to: [
                {
                type: 'actionType',
                }
            ]
        }
    ]
};