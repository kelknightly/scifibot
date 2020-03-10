export default {
    name: 'noun',
    type: 'document',
    title: 'Noun',
    fields: [
        {
            name: 'noun',
            type: 'string',
            title: 'Noun',
        },
        {
            name: 'nounType',
            type: 'reference',
            to: [
                {
                    type: 'nounType',
                },
            ]
        }
    ]
};