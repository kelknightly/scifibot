export default {
    name: 'prepositions',
    type: 'document',
    title: 'Prepositions',
    fields: [
        {
            name: 'prepositions',
            type: 'string',
            title: 'Prepositions',
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