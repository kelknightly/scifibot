export default {
    name: 'description',
    type: 'document',
    title: 'Description',
    fields: [
        {
            name: 'description',
            type: 'string',
            title: 'Description',
        },
        {
            name: 'nounType',
            type: 'reference',
            to: [
                {
                    type: 'nounType',
                }
            ]
        },
    ]
};