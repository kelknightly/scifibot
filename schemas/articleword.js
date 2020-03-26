export default {
    name: 'articleword',
    type: 'document',
    title: 'Articleword',
    fields: [
        {
            name: 'articleword',
            type: 'string',
            title: 'Articleword',
        },
        {
            name: 'articleType',
            type: 'reference',
            to: [
                {
                    type: 'articleType',
                },
            ]
        }
    ]
};