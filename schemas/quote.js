export default {
    name: 'quote',
    type: 'document',
    title: 'Quote',
    fields: [
        {
            name: 'quote',
            type: 'string',
            title: 'Quote',
        },
        {
            name: 'author',
            type: 'reference',
            to: [
                {
                    type: 'author',
                }
            ]

        },
        {
            name: 'source',
            type: 'reference',
            to: [
                {
                    type: 'source'
                }
            ]
        }
    ]
};


